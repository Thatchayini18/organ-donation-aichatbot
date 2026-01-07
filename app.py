import streamlit as st

# ---------- ELEGANT AI BACKGROUND ----------
st.markdown("""
<style>
/* Full background */
.stApp {
    background: linear-gradient(135deg,
        #f3e7ff,
        #e6f0ff,
        #fce7f3);
    background-attachment: fixed;
}

/* Glassmorphism container */
.glass-card {
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

/* Chat bubbles */
div[data-testid="stChatMessage"] {
    border-radius: 18px;
    padding: 14px;
    margin-bottom: 10px;
    max-width: 75%;
}

/* User message */
div[data-testid="stChatMessage"][aria-label="user"] {
    background: linear-gradient(135deg, #c7d2fe, #e0e7ff);
    margin-left: auto;
}

/* Assistant message */
div[data-testid="stChatMessage"][aria-label="assistant"] {
    background: rgba(255,255,255,0.85);
    border: 1px solid rgba(255,255,255,0.6);
    margin-right: auto;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #f3e8ff, #e0f2fe);
}
</style>
""", unsafe_allow_html=True)

from chatbot import chatbot_response

# ---------- BACKGROUND & CHAT STYLING ----------
st.markdown("""
<style>
/* Full page background */
.stApp {
    background-color: #f5f7fa;
}

/* Chat bubbles */
div[data-testid="stChatMessage"] {
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}

/* User messages */
div[data-testid="stChatMessage"][aria-label="user"] {
    background-color: #d1e7dd;
}

/* Bot messages */
div[data-testid="stChatMessage"][aria-label="assistant"] {
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
}

/* Sidebar background */
section[data-testid="stSidebar"] {
    background-color: #e9f5f2;
}
</style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="Organ Donation AI Chatbot")

st.title("Organ Donation AI Assistant")

st.markdown("""
<div class="glass-card">
    <h3>🤖 Your AI Health Assistant</h3>
    <p>
    I am here to guide you through organ donation, registration,
    recipient priority, and matching — clearly and compassionately.
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🫀 Donor Help"):
        st.session_state.messages.append({
            "role": "assistant",
            "content": "I can help you understand donor eligibility, safety, and registration."
        })

with col2:
    if st.button("🏥 Recipient Help"):
        st.session_state.messages.append({
            "role": "assistant",
            "content": "I will explain recipient priority, matching, and waiting process."
        })

with col3:
    if st.button("🔄 Matching Info"):
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Let me explain how organ matching works using AI and medical rules."
        })

st.markdown("</div>", unsafe_allow_html=True)


st.caption("24×7 Support for Donors and Recipients")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask your question here...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = chatbot_response(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()

if st.button("🔄 Clear Chat"):
    st.session_state.messages = []
    st.rerun()
