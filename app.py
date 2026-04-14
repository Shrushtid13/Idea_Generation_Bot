from flask import Flask, request, jsonify
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os
from dotenv import load_dotenv

load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

app = Flask(__name__)

# Mistral API key

client = MistralClient(api_key=MISTRAL_API_KEY)

# --- System Prompt (defines bot personality) ---
SYSTEM_PROMPT = """
You are 'IdeaMate' — a friendly, insightful corporate assistant.
Your job is to help users brainstorm, generate ideas, and give thoughtful opinions or suggestions
on business topics, projects, corporate presentations, innovation, and more.

Guidelines:
- Be conversational and professional.
- Give creative yet practical suggestions.
- If asked for ideas, provide a few varied examples.
- If asked for advice, explain reasoning clearly.
- Keep responses natural — like a chat, not a report or PPT.

Example:
User: "Suggest ideas for a new employee engagement program"
You: "You could try monthly innovation challenges, a peer-recognition app, or mini cross-department events. 
People love things that make them feel visible and valued!"
"""

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    # Send to Mistral
    response = client.chat(
        model="mistral-large-latest",
        messages=[
            ChatMessage(role="system", content=SYSTEM_PROMPT),
            ChatMessage(role="user", content=user_message)
        ]
    )

    bot_reply = response.choices[0].message.content
    return jsonify({"reply": bot_reply})


if __name__ == '__main__':
    app.run(debug=True)
