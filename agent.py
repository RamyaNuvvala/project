import streamlit as st
import random

# Define responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "college": ["Our college offers a variety of programs. What specific information are you looking for?"],
    # Add more responses as needed
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    st.title("College Information Chatbot")
    st.markdown("Welcome to our college chatbot! Ask me anything about our college.")

    user_input = st.text_input("You:", "")
    if st.button("Send"):
        if user_input:
            bot_response = chatbot_response(user_input)
            st.write(f"You: {user_input}")
            st.write(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()
            
