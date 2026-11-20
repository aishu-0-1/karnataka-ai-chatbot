
import streamlit as st
from rag_engine import get_answer

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="Karnataka AI Chatbot",
    page_icon="🌿",
    layout="wide"
)

# =====================================================
# 2. CHAT SESSION
# =====================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================================
# 3. CUSTOM CSS
# =====================================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #faf3ff, #fff0f7, #edf7ff);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #351254, #6634a5, #8a58c9);
}

[data-testid="stSidebar"] * {
    color: white;
}

.main-heading {
    text-align: center;
    color: #682d96;
    font-size: 38px;
    font-weight: 900;
}

.hero {
    background: linear-gradient(135deg, #f5ddff, #ffe5f3, #e3f4ff);
    padding: 32px 20px;
    border-radius: 24px;
    border: 1px solid #ead3ff;
    text-align: center;
    margin: 15px 0 25px 0;
}

.hero-subtitle {
    color: #b24894;
    font-size: 23px;
    font-weight: 700;
    font-style: italic;
}

.hero-description {
    color: #665374;
    font-size: 15px;
}

.topic-card {
    padding: 22px 12px;
    border-radius: 20px;
    min-height: 185px;
    text-align: center;
    margin-bottom: 12px;
}

.topic-card h2 {
    font-size: 35px;
}

.topic-card h4 {
    font-size: 17px;
}

.topic-card p {
    font-size: 13px;
}

.history-card {
    background: linear-gradient(135deg, #efd8ff, #f7eaff);
    color: #70339a;
}

.geography-card {
    background: linear-gradient(135deg, #d6f6df, #eaffed);
    color: #287b49;
}

.culture-card {
    background: linear-gradient(135deg, #ffe1c4, #fff0d9);
    color: #a75b23;
}

.economy-card {
    background: linear-gradient(135deg, #d8edff, #eaf6ff);
    color: #2d70a7;
}

.chat-heading {
    color: #6d3198;
    font-weight: 800;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# 4. TEAM MEMBERS
# =====================================================
team_members = [
    "Jyothi",
    "Aishwarya",
    "Chaithra B H",
    "Madava"
]

# =====================================================
# 5. SIDEBAR
# =====================================================
with st.sidebar:

    st.markdown("# 🌿 Karnataka AI")
    st.markdown("### Knowledge Assistant")
    st.caption("Explore Karnataka's 31 Districts")
    st.markdown("---")

    # PROJECT PIPELINE
    with st.expander("⚙️ Project Pipeline"):

        st.markdown("### 🔄 How It Works")

        st.markdown("""
**1. Data Collection**  
Collect information about Karnataka districts.

**2. Knowledge Base**  
Organize information into four topic files.

**3. Text Processing**  
Read and process stored information.

**4. District Detection**  
Identify the district mentioned in the question.

**5. Topic Detection**  
Identify the topic of the question.

**6. Information Retrieval**  
Retrieve the matching district information.

**7. Answer Preparation**  
Prepare the answer from retrieved information.

**8. Chatbot Response**  
Display the answer to the user.
""")

    # PROJECT INFO
    with st.expander("ℹ️ Project Info"):

        st.markdown("### 💜 About Project")

        st.write("""
Karnataka AI Chatbot is an interactive knowledge assistant
that provides district-based information about Karnataka.

Users can explore history, geography, culture, tourism,
economy and development through simple questions.
""")

        st.markdown("---")
        st.markdown("### 🎯 Project Objectives")

        st.markdown("""
- Provide district-specific information.
- Cover Karnataka's 31 districts.
- Organize information into four topics.
- Make district information easy to explore.
- Answer users' district-related questions.
""")

        st.markdown("---")
        st.markdown("### 📚 Topics")

        st.markdown("""
**🏛️ History & Heritage**  
Historical places, dynasties and heritage.

**🌄 Geography & Natural Resources**  
Rivers, climate, landscapes and resources.

**🎭 Culture & Tourism**  
Festivals, traditions, tourist places and food.

**📈 Economy & Development**  
Agriculture, industries and regional development.
""")

        st.markdown("---")
        st.markdown("### 💻 Technologies Used")

        st.markdown("""
- Python
- Streamlit
- Text-based knowledge files
- District and topic retrieval
""")

        st.markdown("---")
        st.markdown("### 👥 Team Members")

        for number, member in enumerate(team_members, start=1):
            st.markdown(f"**{number}. {member}**")

        st.markdown("---")
        st.caption("Computer Science and Engineering")
        st.caption("Shridevi Institute of Engineering and Technology")

    st.markdown("---")
    st.caption("📍 Karnataka, India")
    st.caption("31 Districts • 4 Topics")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# =====================================================
# 6. MAIN HOME PAGE
# =====================================================

st.markdown("""
<div class="main-heading">
🌿 Karnataka AI Chatbot
</div>
""", unsafe_allow_html=True)

# WELCOME BANNER
st.markdown("""
<div class="hero">
<div class="hero-subtitle">Your Karnataka Knowledge Assistant</div>
<div class="hero-description">
Discover the beauty, history and culture of Karnataka ✨
</div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# 7. EXPLORE TOPICS
# =====================================================
st.markdown(
    "<h3 style='text-align:center;color:#8a48b5;'>✨ Explore Topics ✨</h3>",
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
<div class="topic-card history-card">
<h2>🏛️</h2>
<h4>History & Heritage</h4>
<p>Discover Karnataka's history and heritage.</p>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="topic-card geography-card">
<h2>🌄</h2>
<h4>Geography</h4>
<p>Explore landscapes and natural resources.</p>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="topic-card culture-card">
<h2>🎭</h2>
<h4>Culture & Tourism</h4>
<p>Discover traditions and tourist places.</p>
</div>
""", unsafe_allow_html=True)

with col4:
    st.markdown("""
<div class="topic-card economy-card">
<h2>📈</h2>
<h4>Economy & Development</h4>
<p>Explore industries and development.</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# 8. CHAT AREA
# =====================================================
st.markdown("---")

st.markdown(
    "<h3 class='chat-heading'>💬 Ask Karnataka AI</h3>",
    unsafe_allow_html=True
)

st.caption("Ask a question about any of Karnataka's 31 districts.")

# DISPLAY PREVIOUS MESSAGES
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# CHAT INPUT
question = st.chat_input("Ask about Karnataka districts...")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("🌿 Searching Karnataka information..."):
            try:
                answer = get_answer(question)
            except Exception as error:
                answer = "Sorry, an error occurred while processing your question."
                st.error(str(error))

        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
