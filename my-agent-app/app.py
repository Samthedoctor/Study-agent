from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import uuid
import json

app = Flask(__name__)
CORS(app)

LANGGRAPH_API_URL = "http://127.0.0.1:2024"

# 1. The URL is ALWAYS /threads. This is the only endpoint we will use.
THREADS_URL = f"{LANGGRAPH_API_URL}/threads"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    thread_id = data.get('thread_id') or str(uuid.uuid4())

    # 2. We build the entire complex payload that the API expects.
    # Our message goes deep inside the "values" list.
    payload = {
        "thread_id": thread_id,
        "supersteps": [
            {
                "updates": [
                    {
                        "values": [
                            {"role": "user", "content": user_message}
                        ]
                    }
                ]
            }
        ]
    }

    print(f"Sending to LangGraph URL: {THREADS_URL}")
    print(f"Payload: {payload}")

    # The POST to /threads returns a stream of events, so this logic remains.
    with requests.post(THREADS_URL, json=payload, stream=True) as response:
        response.raise_for_status()

        agent_responses = []
        for line in response.iter_lines():
            if line:
                line_str = line.decode('utf-8')
                if line_str.startswith('data: '):
                    if "[DONE]" in line_str:
                        break
                    json_str = line_str[len('data: '):]
                    agent_responses.append(json.loads(json_str))

    print(f"Received from LangGraph: {agent_responses}")

    # The thread ID is now inside the first event of the response stream
    new_thread_id = agent_responses[0].get("thread_id") if agent_responses else thread_id
    
    final_response = next((
        msg for msg in reversed(agent_responses)
        if msg.get("role") == "assistant" and msg.get("content")
    ), None)

    return jsonify({
        "response": final_response['content'] if final_response else "The agent finished but sent no message.",
        "thread_id": new_thread_id
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)