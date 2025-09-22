import streamlit as st
from study_dep import graph, GraphState
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from typing import List, Dict, Any

# Set up the title of your app
st.title("LangGraph Chatbot with Tool Calls")

# Initialize chat history and state in Streamlit's session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    # Use different chat message containers for different roles
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)
            # Display subjects if they exist in the state
            if message.additional_kwargs and message.additional_kwargs.get("subjects"):
                st.write(f"Updated subjects list: {message.additional_kwargs['subjects']}")
    elif isinstance(message, ToolMessage):
        with st.chat_message("tool_output"):
            st.markdown(f"**Tool Output:** `{message.content}`")


# Accept user input
if prompt := st.chat_input("What would you like to add or delete?"):
    # Add user message to chat history
    st.session_state.messages.append(HumanMessage(content=prompt))
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        current_subjects = []

        # Prepare the input for the graph.
        # This will be used to initialize the state.
        inputs = {"messages": [HumanMessage(content=prompt)]}
        
        # Stream the response from the LangGraph workflow
        # The `stream()` method yields events as the graph executes
        for event in graph.stream(inputs):
            # The event contains the state updates from each node
            for key, value in event.items():
                if key == "subjects":
                    current_subjects = value
                    # You can show the updated subjects list here if you want real-time updates
                
                # Check if the event came from the 'agent' node
                if key == 'agent':
                    # Get the message from the agent's output
                    ai_message = value.get("messages")[-1]
                    # Update the full response with the new content
                    full_response += getattr(ai_message, 'content', '')

                    # Add an indication that the agent is thinking
                    message_placeholder.markdown(full_response + "▌")
                
                # Check if the event came from the 'tools' node
                if key == 'tools':
                    tool_output = value.get("messages")[-1]
                    # Display the tool output in a separate message container
                    with st.chat_message("tool_output"):
                        st.markdown(f"**Tool Output:** `{tool_output.content}`")
        
        # Once streaming is complete, show the final response
        message_placeholder.markdown(full_response)
        
    # Store the assistant's final response in chat history
    # This also includes any tool output if your agent workflow returns it
    final_message = AIMessage(content=full_response, additional_kwargs={"subjects": current_subjects})
    st.session_state.messages.append(final_message)
