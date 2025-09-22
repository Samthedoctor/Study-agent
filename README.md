# Study Agent 🧠✨

![Status](https://img.shields.io/badge/status-active-green)

An intelligent, AI-powered agent designed to help students organize their academic life. This project uses a stateful agent architecture built with **LangGraph** to provide a personalized and persistent study planning experience.

This project is feature-complete and is actively maintained.

***

## 🎯 Core Idea

The goal of Study Agent is to be a one-stop solution for students to manage their subjects, track their progress, and plan their schedules. By leveraging the power of LLMs through LangChain and LangGraph, the agent can understand natural language commands and maintain a memory of a student's academic profile.

***

## ✨ Features

* **🎓 Academic Management:**
    * Add, update, and delete subjects and their specific topics.
* **📅 Smart Scheduling:**
    * Plan class days and set quiz dates for different topics.
* **📈 Progress & Attendance:**
    * Log study progress for exams and track class attendance.
* **🤖 Intelligent Planning:**
    * Generate personalized study plans based on your deadlines and progress.
* **🔔 Notifications:**
    * Receive reminders for classes, quizzes, and study sessions.

***

## 🎬 Demo

Here's a short video of the Study Agent in action, managing calendar-related tasks:

[**Watch the Demo on Google Drive**](https://drive.google.com/file/d/1gWhxTA3S-kmCunlEvKUi2OEF8fYM-GR0/view?usp=sharing)

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
    git clone [https://github.com/Samthedoctor/Study-agent.git](https://github.com/Samthedoctor/Study-agent.git)
    cd Study-agent
    ```
    *(Note: I've used your actual repository URL here.)*

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
