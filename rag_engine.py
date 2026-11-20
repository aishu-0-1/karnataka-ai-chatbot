
import os
import re

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")


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


def create_chunks(documents):
    chunks = []

    for document in documents:
        paragraphs = document.split("\n")

        for paragraph in paragraphs:
            paragraph = paragraph.strip()

            if len(paragraph) > 30:
                chunks.append(paragraph)

    return chunks


def retrieve(question, chunks):
    words = re.findall(r"\b[a-zA-Z]{3,}\b", question.lower())

    scored_chunks = []

    for chunk in chunks:
        text = chunk.lower()

        score = sum(1 for word in words if word in text)

        if score > 0:
            scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda item: item[0], reverse=True)

    return [chunk for score, chunk in scored_chunks[:5]]


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

    return "\n".join(
        f"{i}. {point}" for i, point in enumerate(points, start=1)
    )


def get_answer(question):
    documents = load_documents()

    if not documents:
        return "No Karnataka information files found."

    chunks = create_chunks(documents)

    results = retrieve(question, chunks)

    return format_answer(results)
