# 💬 IdeaMate — Corporate Suggestion Chatbot

IdeaMate is an intelligent corporate chatbot designed to help users generate ideas, gather feedback, and explore suggestions on business and organizational topics. It provides a conversational interface that enables employees, teams, and stakeholders to brainstorm effectively and make informed decisions.

---

## 🚀 Overview

In modern organizations, idea generation and feedback collection are often fragmented and inefficient. IdeaMate addresses this by offering a real-time, AI-powered conversational assistant that:

- Generates creative and practical business ideas  
- Provides thoughtful suggestions and opinions  
- Enhances collaboration and innovation  
- Improves internal communication  

---

## 🧠 Key Features

- 💡 Idea Generation  
- 💬 Conversational Interface  
- ⚡ Real-time Responses  
- 🤖 AI-Powered (Mistral AI)  
- 📊 Session Memory  

---

## 🏗️ Architecture

User → Streamlit Frontend → Flask API → Mistral AI → Response → User

---

## 🛠️ Tech Stack

- Frontend: Streamlit  
- Backend: Flask (Python)  
- AI Model: Mistral AI  
- Environment: Python 3.12  
- Deployment: Docker  

---

## 📂 Project Structure

IdeaMate/
│
├── app.py
├── server.py
├── requirements.txt
├── .env
├── Dockerfile
├── run.sh
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone Repository
git clone https://github.com/Shrushtid13/Idea_Generation_Bot.git
cd Idea_Generation_Bot

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Configure Environment Variables
Create a .env file:
MISTRAL_API_KEY=your_api_key_here

### 5. Run Backend
python server.py

### 6. Run Frontend
streamlit run app.py

---

## 🔌 API Endpoint

POST /chat

Request:
{
  "message": "Suggest ideas for employee engagement"
}

Response:
{
  "reply": "You could try monthly innovation challenges..."
}

---

## 📌 Use Cases

- Corporate brainstorming  
- Employee engagement strategies  
- Business idea validation  
- Project suggestions  

---

## 🏁 Conclusion

IdeaMate showcases how conversational AI can enhance corporate innovation, streamline idea generation, and improve decision-making processes.
