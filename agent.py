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

    # Use a text area for multiline input
    user_input = st.text_area("You:", "", height=100)

    # Use a button with a custom style
    if st.button("Send", key="send_button", help="Click to send your message", class="stButton"):
        if user_input:
            bot_response = chatbot_response(user_input)
            
            # Display user message
            st.write('<div class="chat-container"><div class="user-message">{}</div></div>'.format(user_input), unsafe_allow_html=True)
            
            # Display bot response
            st.write('<div class="chat-container"><div class="bot-message">{}</div></div>'.format(bot_response), unsafe_allow_html=True)
            
            # Clear the user input
            st.text_area("You:", "", height=100)

            # Request focus on the input area for better UX
            st.experimental_set_query_params(having_input_focus="true")
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()
        
