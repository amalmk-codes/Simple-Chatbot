# Simple AI Chatbot

A simple conversational AI chatbot built using Python and Streamlit.
## Live Demo
https://simple-ai-chatbot-amal.streamlit.app/

## Objective

The objective of this project is to build a simple chatbot that can hold basic conversations with users through a web interface.

## Features

- Simple and clean web interface
- AI-powered responses
- Basic conversation support
- Local responses for common messages
- Personalized responses about the project creator
- Conversation history during the session
- Automatic model selection
- API key protection using environment variables and Streamlit Secrets
- Publicly deployed Streamlit application

## Technologies Used

- Python
- Streamlit
- Google GenAI API
- python-dotenv

## Approach

This project uses a generative AI API through Python and Streamlit.

The chatbot uses three levels of response handling:

1. Personalized responses for questions about the chatbot and its creator.
2. Predefined local responses for common conversations such as greetings and acknowledgements.
3. AI-generated responses for general questions.

This reduces unnecessary API calls for common and personalized messages.

## Project Structure

```text
Simple-Chatbot/
│
├── response.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
