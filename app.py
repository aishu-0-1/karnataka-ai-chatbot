
import streamlit as st
from rag_engine import get_answer

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Karnataka AI Chatbot",
    page_icon="💜",
    layout="wide"
)

# ---------------- DESIGN ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8efff, #f0e6ff, #e7f4ff);
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #38145c, #7541b8, #a56ae0);
}
[data-testid="stSidebar"] * {
    color: white !important;
}
.title {
    font-size: 40px;
    font-weight: 800;
    color: #823ec4;
}
.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #e5d5fa;
    box-shadow: 0 4px 15px rgba(120,70,170,0.12);
    margin-bottom: 15px;
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

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 💜 Karnataka AI")
    st.caption("District Information Chatbot")
    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Home / Chat",
            "⚙️ Project Pipeline",
            "ℹ️ Project Info"
        ]
    )

    st.markdown("---")
    st.caption("🗺️ 31 Districts")
    st.caption("📚 4 Knowledge Topics")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- HOME / CHAT ----------------
if page == "🏠 Home / Chat":

    st.markdown(
        '<div class="title">💜 Karnataka AI Chatbot</div>',
        unsafe_allow_html=True
    )

    st.write("### Your Karnataka District Information Assistant")

    st.markdown("""
    <div class="card">
    👋 Welcome to Karnataka AI Chatbot!<br><br>
    Ask questions about Karnataka districts, history, geography,
    culture, tourism, economy and development.
    </div>
    """, unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask about any Karnataka district...")

    if question:
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Searching district information..."):
                try:
                    answer = get_answer(question)
                except Exception as e:
                    answer = "Sorry, an error occurred."
                    st.error(str(e))

            st.markdown(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

# ---------------- PROJECT PIPELINE ----------------
elif page == "⚙️ Project Pipeline":

    st.markdown(
        '<div class="title">⚙️ Project Pipeline</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
    <h3>About the Project Workflow</h3>
    Karnataka AI Chatbot uses district-based information retrieval
    to answer questions about Karnataka.
    </div>
    """, unsafe_allow_html=True)

    pipeline = [
        ("📥 Step 1 — Data Collection",
         "Collect information about Karnataka and its 31 districts."),
        ("📂 Step 2 — Knowledge Base",
         "Organize information into four topic text files."),
        ("📖 Step 3 — Text Processing",
         "Read and organize the stored district information."),
        ("📍 Step 4 — District Detection",
         "Identify the district name in the user's question."),
        ("📚 Step 5 — Topic Detection",
         "Identify the requested topic such as History or Geography."),
        ("🔎 Step 6 — Information Retrieval",
         "Retrieve the information belonging to the selected district and topic."),
        ("🤖 Step 7 — Answer Generation",
         "Prepare a clear answer using the retrieved information."),
        ("💬 Step 8 — Display Answer",
         "Show the answer to the user through the chatbot interface.")
    ]

    for title, description in pipeline:
        st.markdown(f"""
        <div class="card">
        <h4>{title}</h4>
        <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- PROJECT INFO ----------------
elif page == "ℹ️ Project Info":

    st.markdown(
        '<div class="title">ℹ️ Project Info</div>',
        unsafe_allow_html=True
    )

    # ABOUT
    st.markdown("""
    <div class="card">
    <h2>💜 About the Project</h2>
    Karnataka AI Chatbot is an interactive chatbot designed to provide
    district-specific information about Karnataka. It helps users explore
    the state's history, geography, culture, tourism, economy and development
    through simple questions and answers.
    </div>
    """, unsafe_allow_html=True)

    # OBJECTIVES
    st.markdown("""
    <div class="card">
    <h3>🎯 Project Objectives</h3>
    <ul>
    <li>Provide information about Karnataka's 31 districts.</li>
    <li>Organize district knowledge into different topics.</li>
    <li>Retrieve relevant information based on user questions.</li>
    <li>Make regional information easy to understand and explore.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # TOPICS
    st.markdown("## 📚 Topics")

    topics = [
        ("🏰 History & Heritage",
         "Dynasties, historical places, forts and heritage."),
        ("🌍 Geography & Natural Resources",
         "Rivers, climate, landscapes, soil and natural resources."),
        ("🎭 Culture & Tourism",
         "Festivals, traditions, tourist attractions and local food."),
        ("🏭 Economy & Development",
         "Agriculture, industries, business and regional development.")
    ]

    for title, description in topics:
        st.markdown(f"""
        <div class="card">
        <h4>{title}</h4>
        <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

    # TEAM
    st.markdown("## 👥 Team Members")

    cols = st.columns(2)

    for i, member in enumerate(team_members):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="card">
            <h3>👤 {member}</h3>
            <p>Karnataka AI Chatbot Project Team</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h4>🎓 Department</h4>
    Computer Science and Engineering<br>
    Shridevi Institute of Engineering and Technology
    </div>
    """, unsafe_allow_html=True)
