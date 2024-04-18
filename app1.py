import streamlit as st
import google.generativeai as genai

# Configure Gemini AI API with your API key
f = open(r"C:\Users\91998\OneDrive\Desktop\Internship_folder\openai_handson\gemini_keys\gemini_key.txt")
key = f.read().strip()  # Remove any leading/trailing white spaces
genai.configure(api_key=key)

# Initialize the Gemini AI GenerativeModel
model = genai.GenerativeModel('gemini-pro')

# Start a chat with the model
chat = model.start_chat(history=[])

# Set page title and description
st.markdown('<h1 style="color: #FFFF00;">📚 Conversational AI Data Science Tutor with Gemini AI 🤖</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:  #FFC0CB; font-size: large;">*Ask your data science questions and get informative answers!* 📘</p>', unsafe_allow_html=True)

if "memory" not in st.session_state:
    st.session_state["memory"] = []

st.chat_message("Geminiai").write("Hello, Enter your Data Science Question")

for msg in st.session_state["memory"]:
    st.chat_message(msg["role"]).write(msg["text"])

user_query = st.chat_input()

if user_query:
    st.session_state["memory"].append({"role": "User", "text": user_query})
    st.chat_message("User").write(user_query)
    
    try:
        # Send the user's question to the model
        response = chat.send_message(user_query)
        
        # Add the chatbot's response to the session state memory
        st.session_state["memory"].append({"role": "Instructor", "text": response.text})
        
        # Display the chatbot's response in the chat interface
        st.chat_message("Instructor").write(response.text)
        
    except Exception as e:
        st.error(f"Error: {e}")
