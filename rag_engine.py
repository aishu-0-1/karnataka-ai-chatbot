
import os

DATA_FOLDER = "data"

def load_documents():
    documents = []

    if not os.path.exists(DATA_FOLDER):
        return documents

    for file in os.listdir(DATA_FOLDER):
        path = os.path.join(DATA_FOLDER, file)

        if os.path.isfile(path) and file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                documents.append(f.read())

    return documents


def get_answer(question):
    documents = load_documents()

    if not documents:
        return "No Karnataka information files found."

    text = "\n".join(documents)
    words = question.lower().split()

    matches = []

    for paragraph in text.split("\n"):
        paragraph = paragraph.strip()

        if any(word in paragraph.lower() for word in words):
            matches.append(paragraph)

    if matches:
        return "\n".join(matches[:8])

    return "Information not found in my Karnataka knowledge base."
