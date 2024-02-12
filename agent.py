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
    .chat-container {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .chat-message {
        margin-bottom: 10px;
    }
    .user-message {
        background-color: #dff0d8;
        border-radius: 10px;
        padding: 10px;
        display: inline-block;
    }
    .bot-message {
        background-color: #d9edf7;
        border-radius: 10px;
        padding: 10px;
        display: inline-block;
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

    # Maintain chat history
    chat_history = []

    # Use a text area for multiline input
    user_input = st.text_area("You:", "", height=100, key="user_input")

    # Use a button with a custom style
    if st.button("Send", help="Click to send your message"):
        if user_input:
            bot_response = chatbot_response(user_input)
            
            # Append user and bot messages to chat history
            chat_history.append(("You", user_input))
            chat_history.append(("Bot", bot_response))
            
            # Display chat history
            for sender, message in chat_history:
                if sender == "You":
                    st.markdown('<div class="chat-container"><div class="user-message">{}</div></div>'.format(message), unsafe_allow_html=True)
                else:
                    st.markdown('<div class="chat-container"><div class="bot-message">{}</div></div>'.format(message), unsafe_allow_html=True)
            
            # Clear the user input
            st.text_area("You:", "", height=100, key="user_input")

            # Request focus on the input area for better UX
            st.experimental_set_query_params(having_input_focus="true")
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()
