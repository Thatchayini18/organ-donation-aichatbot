import streamlit as st
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
import tempfile
import os
from chatbot import chatbot_response

st.set_page_config(page_title="Organ Donation Chatbot", page_icon="🫀")

st.title("🫀 Organ Donation Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Voice input BELOW chat (like ChatGPT)
col1, col2 = st.columns([6,1])

with col1:
    user_text = st.chat_input("Type your question here...")

with col2:
    audio = mic_recorder(start_prompt="🎤", stop_prompt="⏹️", just_once=True)

def voice_to_text(audio_bytes):
    r = sr.Recognizer()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        path = f.name
    with sr.AudioFile(path) as source:
        audio_data = r.record(source)
    os.remove(path)
    return r.recognize_google(audio_data)

# Handle voice
if audio:
    try:
        voice_text = voice_to_text(audio["bytes"])
        st.session_state.messages.append({"role": "user", "content": voice_text})
        reply = chatbot_response(voice_text)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()
    except:
        st.warning("Voice not recognized")

# Handle text
if user_text:
    st.session_state.messages.append({"role": "user", "content": user_text})
    reply = chatbot_response(user_text)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
