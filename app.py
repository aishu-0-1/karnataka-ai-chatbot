
import streamlit as st
from rag_engine import get_answer

st.set_page_config(
    page_title="Karnataka AI Chatbot",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 Karnataka AI Chatbot")
st.subheader("Your Karnataka Knowledge Assistant")

st.write(
    "Explore Karnataka through four topics: History, Geography, "
    "Culture & Tourism, and Economy & Development."
)

# Four main topics
topics = [
    "🏛️ History & Heritage",
    "🌍 Geography & Natural Resources",
    "🎭 Culture & Tourism",
    "💼 Economy & Development"
]

st.markdown("### Explore Topics")

cols = st.columns(4)

for i, topic in enumerate(topics):
    with cols[i]:
        st.info(topic)

st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User question
question = st.chat_input("Ask anything about Karnataka...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    answer = get_answer(question)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.write(answer)
