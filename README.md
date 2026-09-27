# Simple Gemini AI Chatbot

A simple AI chatbot built using Python, Streamlit, and the Google Gemini API.

## Objective

The objective of this project is to create a simple chatbot that can hold basic conversations with users through a web interface.

## Features

- Simple web interface
- AI-generated responses
- Conversation history
- User and chatbot messages
- Secure API key configuration

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- python-dotenv

## Approach

This project uses a Generative AI API approach.

User messages are sent to the Google Gemini model through the Gemini API. The generated response is displayed in the Streamlit web interface.

## Project Structure

```text
Simple-Chatbot/
|
|-- generate.py
|-- gemini.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- .env.example
|-- .env
`-- venv/
```

## Installation

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a file named `.env` in the project folder.

Add:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

Do not upload the `.env` file to GitHub.

### 5. Run the chatbot

```bash
streamlit run gemini.py
```

## API Key Security

The Gemini API key is stored in a `.env` file.

The `.env` file is included in `.gitignore, so the API key is not uploaded to GitHub.

## Challenges Faced

One challenge was configuring the Gemini API and keeping the API key secure.

This was solved by using a `.env` file and adding `.env` to `.gitignore`.

## Future Improvements

- Add multiple chatbot personalities
- Add conversation export
- Add voice input
- Add voice responses
- Deploy the chatbot online
- Add custom knowledge using RAG

## Author

AMAL M K

BTech Computer Science and Engineering

## uLearn Task

Build a Simple Chatbot

Hashtag: #cl-ai-chatbot
