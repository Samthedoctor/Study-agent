# Study Agent 🧠✨

![Status](https://img.shields.io/badge/status-in%20progress-yellow)

An intelligent, AI-powered agent designed to help students organize their academic life. This project uses a stateful agent architecture built with **LangGraph** to provide a personalized and persistent study planning experience.

This is an **ongoing project**. The core foundation is being built, and new features will be added incrementally.

***

## 🎯 Core Idea

The goal of Study Agent is to be a one-stop solution for students to manage their subjects, track their progress, and plan their schedules. By leveraging the power of LLMs through LangChain and LangGraph, the agent can understand natural language commands and maintain a memory of a student's academic profile.

***

## ✨ Features

### ✅ Currently Implemented

These are the features that are currently working in the project:

* **Subject Management:**
    * Add new subjects to your academic profile.
    * Update the names of existing subjects.
    * Delete subjects you no longer need.
* **Topic Management:**
    * Add specific topics under each subject.
    * Update the details of any topic.
    * Delete topics from a subject.

### 🚀 Planned Features (Roadmap)

This is where the project is heading:

* **📅 Smart Scheduling:** Plan which days to hold classes or take quizzes for specific topics.
* **📈 Progress Tracking:** Log how much you've studied for an upcoming quiz or exam.
* **✅ Attendance Monitoring:** Keep a simple log of your attendance for different subjects.
* **🤖 Personalized Plans:** Generate study plans based on upcoming deadlines and your recorded progress.
* **🔔 Notification System:** Get reminders for upcoming classes, quizzes, and study sessions.

***

## 🛠️ Tech Stack

* **Agent Framework:** **LangChain** & **LangGraph** are used to create the core stateful, multi-agent logic.
* **Database:** **MongoDB** serves as the persistent memory backend for the LangGraph state, ensuring that your data (subjects, topics, etc.) is saved across sessions.
* **LLM:** **Google Gemini** is the Large Language Model that powers the agent's intelligence and natural language understanding.



***

## ⚙️ Getting Started

Follow these steps to get the project running on your local machine.

### Prerequisites

* Python 3.10+
* Git

### 🚀 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/study-agent.git](https://github.com/your-username/study-agent.git)
    cd study-agent
    ```
    *(Replace `your-username/study-agent.git` with your actual repository URL)*

2.  **Create and Activate a Virtual Environment**
    * On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install Required Packages**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables**
    * Create a new file named `.env` in the root directory of the project.
    * Add your Google Gemini API key to this file. **It is crucial to keep this key private and not commit it to version control.**
        ```
        GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"
        ```

### ▶️ Running the Agent

With your virtual environment activated and the `.env` file in place, run the following command in your terminal:

```bash
langgraph dev
