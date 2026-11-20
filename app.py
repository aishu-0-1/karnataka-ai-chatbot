```python
import streamlit as st
from rag_engine import get_answer

st.set_page_config(
    page_title="Karnataka AI Chatbot",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 Karnataka AI Chatbot")
st.subheader("Your Karnataka Knowledge Assistant")

st.write(
    "Explore Karnataka through four topics: "
    "History, Geography, Culture & Tourism, and Economy & Development."
)

topics = [
    "History & Heritage",
    "Geography & Natural Resources",
    "Culture & Tourism",
    "Economy & Development"
]

st.markdown("### Explore Topics")

for topic in topics:
    st.markdown(f"🌱 **{topic}**")

st.markdown("---")
st.markdown("### 💬 Ask a Question")

question = st.text_input(
    "Ask anything about Karnataka:"
)

if st.button("Submit Question"):
    if question.strip():
        with st.spinner("Finding your answer..."):
            answer = get_answer(question)

        st.markdown("### Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question first.")
```
