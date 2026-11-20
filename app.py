
import streamlit as st
from rag_engine import get_answer

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Karnataka AI Chatbot",
    page_icon="💜",
    layout="wide"
)

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8efff, #f0e6ff, #e7f4ff);
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #32104f, #6637a5, #8957c9);
}
[data-testid="stSidebar"] * {
    color: white;
}
.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #873ec4;
}
.info-card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    border: 1px solid #e7d7fa;
    box-shadow: 0 4px 12px rgba(100, 60, 150, 0.12);
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TEAM MEMBERS ----------------
team_members = [
    "Jyothi",
    "Aishwarya",
    "Chaithra B H",
    "Madava"
]

# ---------------- CHAT HISTORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.markdown("# 💜 Karnataka AI")
    st.caption("AI Tourism & District Information Assistant")
    st.markdown("---")

    # PROJECT PIPELINE
    with st.expander("⚙️ Project Pipeline", expanded=False):
        st.markdown("### How the chatbot works")

        st.markdown("""
        **1. Data Collection**  
        Collect Karnataka district information.

        **2. Knowledge Base**  
        Organize information into 4 topic files.

        **3. Text Processing**  
        Read and process the stored text.

        **4. District Detection**  
        Identify the district from the user's question.

        **5. Topic Detection**  
        Identify the topic being asked.

        **6. Information Retrieval**  
        Retrieve the matching district information.

        **7. Answer Generation**  
        Prepare a relevant answer.

        **8. Chatbot Response**  
        Display the answer to the user.
        """)

    # PROJECT INFO
    with st.expander("ℹ️ About Project", expanded=False):
        st.markdown("### 📌 About Project")

        st.write("""
        Karnataka AI Chatbot is an interactive assistant that provides
        information about Karnataka districts. It helps users explore
        history, geography, culture, tourism and development.
        """)

        st.markdown("---")
        st.markdown("### 🎯 Project Objectives")

        st.markdown("""
        - Provide district-specific information.
        - Cover all 31 Karnataka districts.
        - Organize information into different topics.
        - Make information easy for users to explore.
        """)

    # TECHNOLOGIES
    with st.expander("💻 Technologies Used", expanded=False):
        st.markdown("""
        - 🐍 Python
        - 🌐 Streamlit
        - 📄 Text files
        - 🔎 Information retrieval
        - 🤖 AI question-answering interface
        """)

    # TOPICS
    with st.expander("📚 Project Topics", expanded=False):
        st.markdown("""
        **🏰 History & Heritage**  
        Historical places, dynasties and heritage.

        **🌍 Geography & Natural Resources**  
        Rivers, climate, landscape and natural resources.

        **🎭 Culture & Tourism**  
        Festivals, traditions, tourist places and local food.

        **🏭 Economy & Development**  
        Agriculture, industries and economic development.
        """)

    # TEAM MEMBERS
    with st.expander("👥 Team Members", expanded=False):
        st.markdown("### Our Project Team")

        for i, member in enumerate(team_members, start=1):
            st.markdown(f"**{i}. 👤 {member}**")

        st.markdown("---")
        st.caption("Computer Science and Engineering")
        st.caption("Shridevi Institute of Engineering and Technology")

    st.markdown("---")
    st.caption("📍 Karnataka, India")
    st.caption("31 Districts • 4 Topics")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ---------------- MAIN CHAT PAGE ----------------
st.markdown(
    '<div class="main-title">💜 Karnataka AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown("### Explore Karnataka, one question at a time.")

st.markdown("""
<div class="info-card">
<b>Welcome! 👋</b><br><br>
Ask about Karnataka districts, history, geography, culture, tourism,
economy and development.
</div>
""", unsafe_allow_html=True)

# ---------------- DISPLAY CHAT HISTORY ----------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- CHAT INPUT ----------------
question = st.chat_input("Ask about any Karnataka district...")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching Karnataka information..."):
            try:
                answer = get_answer(question)
            except Exception as e:
                answer = "Sorry, an error occurred while processing your question."
                st.error(str(e))

        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
