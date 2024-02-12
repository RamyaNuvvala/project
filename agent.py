import streamlit as st
import random

# Define responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "college": ["Our college offers a variety of programs. What specific information are you looking for?"],
    # Add more responses as needed
}

# Custom styling
st.markdown(
    """
    <style>
    .stTextInput > div > div > input {
        background-color: #f0f0f0;
        border: none;
        border-radius: 10px;
        padding: 10px;
        width: 100%;
    }
    .stButton> button {
        border-radius: 10px;
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }
    .stText {
        color: #333333;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    st.title("College Information Chatbot")
    st.markdown("Welcome to our college chatbot! Ask me anything about our college.")

    # Use a text area for multiline input
    user_input = st.text_area("You:", "", height=100)

    # Use a button with a custom style
    if st.button("Send", key="send_button", help="Click to send your message"):
        if user_input:
            bot_response = chatbot_response(user_input)
            st.text_area("Bot:", value=bot_response, height=100, max_chars=None, key=None)
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()
            
