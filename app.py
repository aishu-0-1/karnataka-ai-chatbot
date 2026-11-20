
import streamlit as st

st.set_page_config(
    page_title="Karnataka AI Chatbot",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 Karnataka AI Chatbot")
st.subheader("Your Karnataka Knowledge Assistant")

st.write(
    "Ask me about Karnataka's history, geography, "
    "culture, tourism, and economy."
)

# Four main topics
topics = [
    "History & Heritage",
    "Geography & Natural Resources",
    "Culture & Tourism",
    "Economy & Development"
]

st.markdown("### Explore Karnataka")

for topic in topics:
    st.info(topic)

# Chat input
question = st.chat_input("Ask anything about Karnataka...")

if question:
    st.chat_message("user").write(question)

    st.chat_message("assistant").write(
        "Welcome! Your Karnataka chatbot is being developed. "
        "We will add detailed knowledge about Karnataka in the next steps."
    )
