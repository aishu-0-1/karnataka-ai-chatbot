
import streamlit as st
from rag_engine import get_answer

st.set_page_config(
    page_title="Karnataka AI Chatbot",
    page_icon="🏛️",
    layout="wide"
)

# ---------- CUSTOM DESIGN ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f8, #f4eaff, #fff8e8);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    text-align: center;
    padding: 30px 10px;
}

.hero h1 {
    color: #58127d;
    font-size: 48px;
    font-weight: 900;
}

.hero h3 {
    color: #8b3b9f;
    font-style: italic;
}

.hero p {
    font-size: 18px;
    color: #4b3154;
}

.topic-title {
    text-align: center;
    color: #6a168a;
    font-size: 30px;
    font-weight: bold;
    margin: 25px 0;
}

.topic-card {
    border-radius: 22px;
    padding: 20px 12px;
    text-align: center;
    min-height: 190px;
    border: 2px solid rgba(255,255,255,0.8);
    box-shadow: 0 5px 15px rgba(80,30,100,0.12);
}

.topic-card h2 {
    font-size: 38px;
}

.topic-card h3 {
    font-size: 20px;
    margin-bottom: 8px;
}

.topic-card p {
    font-size: 14px;
}

.purple {
    background: linear-gradient(135deg, #f0d5ff, #e9baff);
    color: #56117c;
}

.green {
    background: linear-gradient(135deg, #d8f7dc, #a8e6b0);
    color: #155c2b;
}

.orange {
    background: linear-gradient(135deg, #ffe6c6, #ffc88c);
    color: #914300;
}

.blue {
    background: linear-gradient(135deg, #d5ebff, #a7d3ff);
    color: #124c91;
}

.ask-box {
    background: rgba(255,255,255,0.8);
    border: 2px solid #e5c8f3;
    border-radius: 22px;
    padding: 25px;
    margin-top: 25px;
}

.footer {
    text-align: center;
    color: #6a168a;
    font-size: 18px;
    font-style: italic;
    padding: 25px;
}

.stButton button {
    background: linear-gradient(90deg, #7b1fa2, #a435c7);
    color: white;
    border-radius: 12px;
    border: none;
    height: 48px;
    font-weight: bold;
}

.stButton button:hover {
    background: #571078;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="hero">
    <h1>🌿 Karnataka AI Chatbot</h1>
    <h3>Your Karnataka Knowledge Assistant</h3>
    <p>
        Explore Karnataka through History, Geography, Culture & Tourism,
        and Economy & Development.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- TOPICS ----------
st.markdown(
    '<div class="topic-title">✨ Explore Topics ✨</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="topic-card purple">
        <h2>🏛️</h2>
        <h3>History & Heritage</h3>
        <p>Kings, dynasties and Karnataka history</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="topic-card green">
        <h2>🌄</h2>
        <h3>Geography & Natural Resources</h3>
        <p>Rivers, forests, minerals and nature</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="topic-card orange">
        <h2>🎭</h2>
        <h3>Culture & Tourism</h3>
        <p>Festivals, traditions and tourist places</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="topic-card blue">
        <h2>📈</h2>
        <h3>Economy & Development</h3>
        <p>Industries, technology and growth</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- CHAT SECTION ----------
st.markdown("""
<div class="ask-box">
    <h2>💬 Ask a Question</h2>
    <p>Ask anything about Karnataka!</p>
</div>
""", unsafe_allow_html=True)

question = st.text_input(
    "Your question",
    placeholder="e.g. Tell me about Hampi",
    label_visibility="collapsed"
)

if st.button("✈️ Submit Question", use_container_width=True):
    if question.strip():
        with st.spinner("🔍 Searching Karnataka knowledge..."):
            answer = get_answer(question)

        st.markdown("### 📚 Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    💜 Discover &nbsp; • &nbsp; Learn &nbsp; • &nbsp; Explore Karnataka 🌿
</div>
""", unsafe_allow_html=True)
