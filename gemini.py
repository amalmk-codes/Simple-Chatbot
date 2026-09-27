import os
import random
import streamlit as st
from dotenv import load_dotenv
from google import genai


# ============================================================
# CONFIGURATION
# ============================================================

MAX_RESPONSES = 20

# Internal model list.
# These names are not shown in the frontend.
MODELS = [
    "gemini-3.8-flash",
    "gemini-3.7-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-3.1-pro-preview",
    "gemini-3-flash-preview",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.5-pro"
]


# ============================================================
# LOCAL RESPONSES
# These messages do NOT use the API.
# ============================================================

LOCAL_RESPONSES = {

    # GREETINGS

    "hi": [
        "Hi! 👋 How can I help you?",
        "Hello! 👋 What can I do for you?",
        "Hi there! 😊 Feel free to ask me anything."
    ],

    "hello": [
        "Hello! 👋 How can I help you?",
        "Hi! 😊 What would you like to know?",
        "Hello there! How can I assist you?"
    ],

    "hey": [
        "Hey! 👋 How can I help?",
        "Hey there! 😊 What can I do for you?",
        "Hi! What would you like to talk about?"
    ],

    "heyy": [
        "Hey! 👋 How can I help?",
        "Hello! 😊 What's on your mind?"
    ],

    "heyyy": [
        "Hey! 👋 How can I help?",
        "Hi there! 😊"
    ],

    "hii": [
        "Hi! 👋 How can I help you?",
        "Hello! 😊 What can I do for you?"
    ],

    "hiii": [
        "Hiii! 👋 How can I help?",
        "Hello! 😊"
    ],

    "hiiii": [
        "Hiiii! 👋 How can I help you?"
    ],

    "yo": [
        "Hey! 👋 What's up?",
        "Hi! 😊 How can I help?"
    ],

    "sup": [
        "Hey! 👋 I'm here and ready to help.",
        "Not much! 😊 What can I help you with?"
    ],

    "wassup": [
        "Hey! 👋 I'm ready to help. What's up?",
        "Hello! 😊 What can I do for you?"
    ],


    # GOOD MORNING

    "good morning": [
        "Good morning! ☀️ Have a great day!",
        "Good morning! 😊 How can I help you today?",
        "Good morning! 🌅 What would you like to know?"
    ],

    "goodmorning": [
        "Good morning! ☀️ How can I help you today?"
    ],

    "morning": [
        "Good morning! ☀️ How can I help?",
        "Good morning! 😊"
    ],


    # GOOD AFTERNOON

    "good afternoon": [
        "Good afternoon! 😊 How can I help you?",
        "Good afternoon! ☀️ What can I do for you?"
    ],

    "goodafternoon": [
        "Good afternoon! 😊 How can I help?"
    ],

    "afternoon": [
        "Good afternoon! 😊"
    ],


    # GOOD EVENING

    "good evening": [
        "Good evening! 🌆 How can I help you?",
        "Good evening! 😊 What would you like to know?"
    ],

    "goodevening": [
        "Good evening! 🌆 How can I help?"
    ],

    "evening": [
        "Good evening! 😊"
    ],


    # GOOD NIGHT

    "good night": [
        "Good night! 🌙 Sleep well!",
        "Good night! 😴 Have a peaceful night!",
        "Good night! 🌙 See you again!"
    ],

    "goodnight": [
        "Good night! 🌙 Sleep well!"
    ],

    "night": [
        "Good night! 🌙"
    ],


    # HOW ARE YOU

    "how are you": [
        "I'm doing great! 😊 How can I help you?",
        "I'm good and ready to help! 🤖",
        "I'm doing well! Thanks for asking. 😊"
    ],

    "how are u": [
        "I'm doing great! 😊 How can I help you?",
        "I'm good! 🤖 What can I do for you?"
    ],

    "how r u": [
        "I'm doing great! 😊 Thanks for asking!",
        "I'm good! 🤖 How can I help?"
    ],

    "hru": [
        "I'm doing great! 😊 How can I help?",
        "I'm good! 🤖"
    ],

    "are you okay": [
        "Yes! 😊 I'm ready to help you.",
        "I'm perfectly fine and ready to chat! 🤖"
    ],

    "you okay": [
        "Yes! 😊 I'm ready to help."
    ],


    # THANK YOU

    "thank you": [
        "You're welcome! 😊",
        "You're very welcome! 👍",
        "Happy to help! 😊",
        "Anytime! 🤖"
    ],

    "thanks": [
        "You're welcome! 😊",
        "No problem! 👍",
        "Happy to help!"
    ],

    "thank u": [
        "You're welcome! 😊",
        "No problem! 👍"
    ],

    "thanks a lot": [
        "You're very welcome! 😊",
        "Happy to help!"
    ],

    "thank you so much": [
        "You're very welcome! 😊",
        "Glad I could help! 👍"
    ],

    "thx": [
        "You're welcome! 😊",
        "No problem!"
    ],

    "ty": [
        "You're welcome! 😊"
    ],


    # OK / YES / NO

    "ok": [
        "Okay! 👍",
        "Alright! 😊",
        "Sure! 👍"
    ],

    "okay": [
        "Okay! 👍",
        "Alright! 😊",
        "Sure!"
    ],

    "okk": [
        "Okay! 👍"
    ],

    "okey": [
        "Alright! 👍"
    ],

    "alright": [
        "Alright! 👍",
        "Okay! 😊"
    ],

    "sure": [
        "Sure! 👍",
        "Alright! 😊"
    ],

    "yes": [
        "Great! 👍",
        "Okay! 😊"
    ],

    "yeah": [
        "Alright! 👍",
        "Great! 😊"
    ],

    "yep": [
        "Okay! 👍",
        "Great!"
    ],

    "yup": [
        "Sure! 👍"
    ],

    "no": [
        "Okay! 👍",
        "No problem."
    ],

    "nope": [
        "Okay! 👍",
        "No problem."
    ],


    # BYE

    "bye": [
        "Goodbye! 👋 Have a great day!",
        "Bye! 👋 See you again!",
        "Take care! 😊"
    ],

    "goodbye": [
        "Goodbye! 👋 Take care!",
        "See you again! 😊"
    ],

    "bye bye": [
        "Bye bye! 👋 Take care!",
        "See you again! 😊"
    ],

    "byebye": [
        "Bye bye! 👋"
    ],

    "see you": [
        "See you! 👋 Take care!",
        "See you again! 😊"
    ],

    "see ya": [
        "See ya! 👋"
    ],

    "take care": [
        "You too! 😊 Take care!",
        "Thanks! You take care too. 👋"
    ],


    # WELCOME

    "welcome": [
        "Thank you! 😊",
        "You're welcome! 👍"
    ],

    "you are welcome": [
        "Thank you! 😊"
    ],

    "ur welcome": [
        "Thanks! 😊"
    ],


    # APOLOGY

    "sorry": [
        "No problem! 😊",
        "It's okay! 👍",
        "Don't worry about it!"
    ],

    "my bad": [
        "No problem! 😊",
        "It's okay!"
    ],

    "oops": [
        "No problem! 😊",
        "Oops! It happens. 👍"
    ],


    # LAUGHTER

    "haha": [
        "😄 Haha!",
        "😂 Glad you're having fun!"
    ],

    "hahaha": [
        "😂 Haha!",
        "😄 That's funny!"
    ],

    "lol": [
        "😂 Haha!",
        "😄"
    ],

    "lmao": [
        "😂 Haha!"
    ],

    "hehe": [
        "😊 Hehe!",
        "😄"
    ],


    # UNDERSTANDING

    "got it": [
        "Great! 👍",
        "Awesome! 😊"
    ],

    "i got it": [
        "Great! 👍",
        "Perfect! 😊"
    ],

    "understood": [
        "Great! 👍",
        "Perfect!"
    ],

    "i understand": [
        "Great! 😊",
        "Perfect! 👍"
    ],

    "understand": [
        "Great! 👍"
    ],

    "makes sense": [
        "Great! 😊",
        "Glad it makes sense!"
    ],

    "okay got it": [
        "Great! 👍"
    ],

    "ok got it": [
        "Perfect! 👍"
    ],


    # COMMON CHAT

    "nice": [
        "Glad you liked it! 😊",
        "Awesome! 👍"
    ],

    "great": [
        "Great! 😊",
        "Awesome! 👍"
    ],

    "awesome": [
        "Awesome! 🎉",
        "Glad to hear that! 😊"
    ],

    "cool": [
        "Cool! 😎",
        "Nice! 👍"
    ],

    "perfect": [
        "Perfect! 😊",
        "Great! 👍"
    ],

    "amazing": [
        "Awesome! 😄",
        "Glad you think so! 👍"
    ],

    "wow": [
        "😄 Wow!",
        "Pretty cool, right? 😊"
    ],

    "really": [
        "Yes! 😊",
        "Absolutely!"
    ],

    "really?": [
        "Yes! 😊",
        "Absolutely!"
    ],

    "seriously": [
        "Yes! 😊",
        "Absolutely!"
    ],


    # BOT QUESTIONS

    "who are you": [
        "I'm a simple AI chatbot. 🤖",
        "I'm an AI chatbot built using Python and Streamlit. 🤖"
    ],

    "what are you": [
        "I'm an AI chatbot. 🤖",
        "I'm a simple AI assistant built with Python and Streamlit."
    ],

    "what is your name": [
        "I'm Simple AI Chatbot. 🤖",
        "You can call me AI Chatbot! 😊"
    ],

    "your name": [
        "I'm Simple AI Chatbot. 🤖"
    ],

    "are you a bot": [
        "Yes! 🤖 I'm an AI chatbot."
    ],

    "are you ai": [
        "Yes! 🤖 I'm an AI chatbot."
    ],

    "are you human": [
        "Nope! 🤖 I'm an AI chatbot."
    ],

    "what can you do": [
        "I can answer questions, explain concepts, help with coding, generate ideas, and have conversations with you. 🤖"
    ],


    # HELP

    "help": [
        "Sure! 😊 Ask me a question and I'll try to help.",
        "Of course! 🤖 What do you need help with?"
    ],

    "i need help": [
        "Sure! 😊 Tell me what you need help with."
    ],

    "can you help me": [
        "Of course! 😊 Tell me what you need help with."
    ],

    "please help": [
        "Sure! 🤖 Tell me what you need help with."
    ],


    # TESTING

    "test": [
        "I'm working! ✅",
        "Test successful! 🤖"
    ],

    "testing": [
        "I'm working correctly! ✅"
    ],

    "hello bot": [
        "Hello! 🤖 I'm ready to chat."
    ],

    "hi bot": [
        "Hi! 🤖 How can I help?"
    ],

    "ping": [
        "Pong! 🏓"
    ],


    # EMOJIS

    "👍": [
        "👍",
        "Awesome! 😊"
    ],

    "😊": [
        "😊",
        "Glad to see you smiling!"
    ],

    "😀": [
        "😀 Hello!"
    ],

    "❤️": [
        "❤️ Thank you!"
    ],

    "❤": [
        "❤️ Thank you!"
    ],

    "😂": [
        "😂 Haha!"
    ],

    "🤖": [
        "🤖 Beep boop! I'm here!"
    ]
}


# ============================================================
# NORMALIZE MESSAGE
# ============================================================

def normalize_message(message):

    message = message.strip().lower()

    punctuation = "!?.,;:"

    for character in punctuation:
        message = message.replace(character, "")

    message = " ".join(message.split())

    return message


# ============================================================
# LOCAL RESPONSE
# ============================================================

def get_local_response(message):

    normalized = normalize_message(message)

    if normalized in LOCAL_RESPONSES:
        return random.choice(LOCAL_RESPONSES[normalized])

    return None


# ============================================================
# LOAD ENVIRONMENT
# ============================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# SIMPLE WHITE UI
# ============================================================

st.markdown(
    """
    <style>

    /* =====================================================
       PAGE
       ===================================================== */

    .stApp {
        background: #ffffff !important;
        color: #1f2937 !important;
    }

    [data-testid="stAppViewContainer"] {
        background: #ffffff !important;
    }

    .main {
        background: #ffffff !important;
    }

    .block-container {
        max-width: 850px;
        padding-top: 2rem;
        padding-bottom: 6rem;
    }


    /* =====================================================
       HIDE STREAMLIT EXTRA UI
       ===================================================== */

    [data-testid="stToolbar"] {
        display: none !important;
    }

    [data-testid="stDecoration"] {
        display: none !important;
    }

    [data-testid="stAppDeployButton"] {
        display: none !important;
    }


    /* =====================================================
       HEADER
       ===================================================== */

    .app-header {
        text-align: center;
        padding: 10px 0 28px;
    }

    .app-icon {
        font-size: 42px;
        margin-bottom: 8px;
    }

    .app-title {
        font-size: 30px;
        font-weight: 700;
        color: #111827;
        margin: 0;
    }

    .app-subtitle {
        font-size: 14px;
        color: #6b7280;
        margin-top: 7px;
    }


    /* =====================================================
       WELCOME CARD
       ===================================================== */

    .welcome-card {
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 28px;
        text-align: center;
        margin: 15px auto 20px;
        max-width: 650px;
    }

    .welcome-card h3 {
        color: #111827;
        font-size: 22px;
        margin: 0 0 8px;
    }

    .welcome-card p {
        color: #6b7280;
        font-size: 14px;
        line-height: 1.6;
        margin: 0;
    }


    /* =====================================================
       SUGGESTIONS
       ===================================================== */

    .suggestions {
        text-align: center;
        margin-bottom: 28px;
    }

    .suggestion {
        display: inline-block;
        background: #f3f4f6;
        border: 1px solid #e5e7eb;
        color: #4b5563;
        padding: 7px 12px;
        border-radius: 20px;
        margin: 4px;
        font-size: 12px;
    }


    /* =====================================================
       CHAT MESSAGE
       ===================================================== */

    [data-testid="stChatMessage"] {
        padding: 6px 0 !important;
    }

    [data-testid="stChatMessageContent"] {
        color: #1f2937 !important;
        background: #f8fafc !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 14px !important;
        padding: 12px 16px !important;
        box-shadow: none !important;
    }

    [data-testid="stChatMessageContent"] p {
        color: #1f2937 !important;
        line-height: 1.6 !important;
    }


    /* =====================================================
       USER MESSAGE
       ===================================================== */

    div[data-testid="stChatMessage"]:has(
        [data-testid="stChatMessageAvatarUser"]
    )
    [data-testid="stChatMessageContent"] {

        background: #eff6ff !important;
        border: 1px solid #dbeafe !important;
    }

    div[data-testid="stChatMessage"]:has(
        [data-testid="stChatMessageAvatarUser"]
    )
    [data-testid="stChatMessageContent"] p {

        color: #1e3a8a !important;
    }


    /* =====================================================
       ASSISTANT MESSAGE
       ===================================================== */

    div[data-testid="stChatMessage"]:has(
        [data-testid="stChatMessageAvatarAssistant"]
    )
    [data-testid="stChatMessageContent"] {

        background: #f9fafb !important;
        border: 1px solid #e5e7eb !important;
    }


    /* =====================================================
       CODE BLOCKS
       ===================================================== */

    [data-testid="stChatMessageContent"] pre {
        background: #f3f4f6 !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 10px !important;
    }

    [data-testid="stChatMessageContent"] code {
        color: #111827 !important;
    }


    /* =====================================================
       CHAT INPUT
       ===================================================== */

    [data-testid="stBottom"] {
        background: #ffffff !important;
        border-top: 1px solid #e5e7eb !important;
    }

    [data-testid="stChatInput"] {
        background: #ffffff !important;
        border: 1px solid #d1d5db !important;
        border-radius: 14px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08) !important;
    }

    [data-testid="stChatInput"] textarea {
        color: #111827 !important;
        background: #ffffff !important;
        font-size: 15px !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #9ca3af !important;
    }


    /* =====================================================
       THINKING
       ===================================================== */

    .thinking {
        display: flex;
        align-items: center;
        gap: 5px;
        color: #6b7280;
        font-size: 13px;
    }

    .dot {
        width: 6px;
        height: 6px;
        background: #6b7280;
        border-radius: 50%;
        display: inline-block;
        animation: pulse 1.2s infinite;
    }

    .dot:nth-child(2) {
        animation-delay: 0.2s;
    }

    .dot:nth-child(3) {
        animation-delay: 0.4s;
    }

    @keyframes pulse {
        0%, 60%, 100% {
            opacity: 0.3;
        }

        30% {
            opacity: 1;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# API KEY CHECK
# ============================================================

if not API_KEY:

    st.error("AI service is not configured.")

    st.info(
        "Create a .env file and add your API key."
    )

    st.stop()


# ============================================================
# CLIENT
# ============================================================

client = genai.Client(
    api_key=API_KEY
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "response_count" not in st.session_state:
    st.session_state.response_count = 0


# ============================================================
# HEADER
# ============================================================

st.html(
    """
    <div class="app-header">

        <div class="app-icon">
            🤖
        </div>

        <div class="app-title">
            AI Chatbot
        </div>

        <div class="app-subtitle">
            Simple, helpful and easy to use
        </div>

    </div>
    """
)


# ============================================================
# WELCOME
# ============================================================

if not st.session_state.messages:

    st.html(
        """
        <div class="welcome-card">

            <h3>👋 Welcome!</h3>

            <p>
                Ask a question, learn something new,
                get coding help, or simply start a conversation.
            </p>

        </div>

        <div class="suggestions">

            <span class="suggestion">
                💡 Ask a question
            </span>

            <span class="suggestion">
                💻 Coding help
            </span>

            <span class="suggestion">
                📚 Learning
            </span>

            <span class="suggestion">
                🚀 Project ideas
            </span>

        </div>
        """
    )


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    if message["role"] == "user":
        avatar = "👤"
    else:
        avatar = "🤖"

    with st.chat_message(
        message["role"],
        avatar=avatar
    ):

        st.markdown(
            message["content"]
        )


# ============================================================
# RESPONSE LIMIT
# ============================================================

if st.session_state.response_count >= MAX_RESPONSES:

    st.warning(
        "This chat session has reached its response limit."
    )

    st.info(
        "Please start a new session later."
    )

    st.stop()


# ============================================================
# CHAT INPUT
# ============================================================

prompt = st.chat_input(
    "Type your message..."
)


# ============================================================
# HANDLE MESSAGE
# ============================================================

if prompt:

    # ========================================================
    # LOCAL RESPONSE
    # ========================================================

    local_answer = get_local_response(prompt)

    if local_answer:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message(
            "user",
            avatar="👤"
        ):

            st.markdown(prompt)


        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": local_answer
            }
        )

        with st.chat_message(
            "assistant",
            avatar="🤖"
        ):

            st.markdown(local_answer)


        st.rerun()


    # ========================================================
    # AI RESPONSE
    # ========================================================

    else:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message(
            "user",
            avatar="👤"
        ):

            st.markdown(prompt)


        # ----------------------------------------------------
        # CONVERSATION
        # ----------------------------------------------------

        conversation = ""

        for message in st.session_state.messages:

            role = message["role"].capitalize()

            content = message["content"]

            conversation += (
                f"{role}: {content}\n"
            )


        # ----------------------------------------------------
        # RESPONSE
        # ----------------------------------------------------

        with st.chat_message(
            "assistant",
            avatar="🤖"
        ):

            thinking_placeholder = st.empty()

            thinking_placeholder.markdown(
                """
                <div class="thinking">
                    <span>Thinking</span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                </div>
                """,
                unsafe_allow_html=True
            )

            answer = None


            # ------------------------------------------------
            # AUTOMATIC MODEL SELECTION
            # ------------------------------------------------

            for model in MODELS:

                try:

                    response = client.models.generate_content(
                        model=model,
                        contents=conversation
                    )

                    if response.text:

                        answer = response.text

                        break

                except Exception:

                    continue


            thinking_placeholder.empty()


            # ------------------------------------------------
            # SHOW RESPONSE
            # ------------------------------------------------

            if answer:

                st.markdown(answer)

            else:

                st.error(
                    "⚠️ Sorry, I could not get a response right now."
                )


        # ----------------------------------------------------
        # SAVE RESPONSE
        # ----------------------------------------------------

        if answer:

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.session_state.response_count += 1

            st.rerun()