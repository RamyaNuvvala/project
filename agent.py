import streamlit as st

def main():
    st.title("College Information Website with Chatbot")
    st.markdown("# Welcome to Our College Information Website!")

    # Add your content here

    # Dialogflow Messenger
    st.markdown("## College Chatbot")
    st.markdown("""
    <iframe
        allow="microphone;"
        width="350"
        height="430"
        src="https://console.dialogflow.com/api-client/demo/embedded/84ec9eb3-eb15-4185-81d9-317b1a5f3d70">
    </iframe>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

