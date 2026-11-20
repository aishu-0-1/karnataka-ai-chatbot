
import os
import re

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")


# 1. Load knowledge files
def load_documents():
    documents = []

    if not os.path.exists(DATA_FOLDER):
        return documents

    for file in os.listdir(DATA_FOLDER):
        path = os.path.join(DATA_FOLDER, file)

        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                documents.append(f.read())

    return documents


# 2. Split documents into small paragraphs
def create_chunks(documents):
    chunks = []

    for document in documents:
        paragraphs = document.split("\n")

        for paragraph in paragraphs:
            paragraph = paragraph.strip()

            if paragraph:
                chunks.append(paragraph)

    return chunks


# 3. Find relevant information
def retrieve(question, chunks):
    stop_words = {
        "what", "when", "where", "which", "who", "why", "how",
        "tell", "about", "the", "and", "for", "from", "are",
        "was", "is", "its", "this", "that", "can", "give"
    }

    question_words = set(
        re.findall(r"\b[a-zA-Z]{3,}\b", question.lower())
    )

    question_words -= stop_words

    scored_chunks = []

    for chunk in chunks:
        chunk_words = set(
            re.findall(r"\b[a-zA-Z]{3,}\b", chunk.lower())
        )

        score = len(question_words & chunk_words)

        if score > 0:
            scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda item: item[0], reverse=True)

    return [chunk for score, chunk in scored_chunks[:3]]


# 4. Format answer into maximum 2 points
def format_answer(chunks):
    if not chunks:
        return "Information not found in my Karnataka knowledge base."

    points = []

    for chunk in chunks:
        sentences = re.split(r"(?<=[.!?])\s+", chunk.strip())

        for sentence in sentences:
            sentence = sentence.strip()

            if sentence and sentence not in points:
                points.append(sentence)

    points = points[:2]

    return "\n".join(
        f"{i}. {point}"
        for i, point in enumerate(points, start=1)
    )


# 5. Main chatbot function
def get_answer(question):
    documents = load_documents()

    if not documents:
        return "No Karnataka information files found."

    chunks = create_chunks(documents)

    results = retrieve(question, chunks)

    answer = format_answer(results)

    return answer
