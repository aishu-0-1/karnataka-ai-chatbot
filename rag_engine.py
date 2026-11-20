
import os
import re

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")


# 1. Load knowledge files with their topic names
def load_documents():
    documents = {}

    if not os.path.exists(DATA_FOLDER):
        return documents

    for file in os.listdir(DATA_FOLDER):
        path = os.path.join(DATA_FOLDER, file)

        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                topic = file.replace(".txt", "").lower()
                documents[topic] = f.read()

    return documents


# 2. Split documents into small paragraphs
def create_chunks(documents):
    chunks = []

    for topic, document in documents.items():
        paragraphs = document.split("\n")

        for paragraph in paragraphs:
            paragraph = paragraph.strip()

            if paragraph:
                chunks.append((topic, paragraph))

    return chunks


# 3. Identify the question topic
def detect_topic(question):
    question = question.lower()

    if any(word in question for word in [
        "history", "dynasty", "king", "kingdom", "empire",
        "tipu", "sultan", "vijayanagara", "gangas",
        "rashtrakuta", "chalukya", "kempegowda"
    ]):
        return "history"

    if any(word in question for word in [
        "river", "mountain", "waterfall", "dam", "geography",
        "forest", "soil", "natural resource", "climate",
        "jog falls", "location"
    ]):
        return "geography"

    if any(word in question for word in [
        "culture", "tourism", "festival", "dasara", "dance",
        "food", "temple", "tourist", "hampi", "mysuru palace"
    ]):
        return "culture_tourism"

    if any(word in question for word in [
        "economy", "development", "industry", "industries",
        "agriculture", "crop", "it sector", "software",
        "company", "employment", "business"
    ]):
        return "economy_development"

    return None


# 4. Retrieve relevant information from the correct topic
def retrieve(question, chunks):
    stop_words = {
        "what", "when", "where", "which", "who", "why", "how",
        "tell", "about", "the", "and", "for", "from", "are",
        "was", "is", "its", "this", "that", "can", "give",
        "in", "of", "to", "on", "do", "does", "me"
    }

    question_words = set(
        re.findall(r"\b[a-zA-Z]{3,}\b", question.lower())
    )

    question_words -= stop_words

    topic = detect_topic(question)

    scored_chunks = []

    for chunk_topic, chunk in chunks:

        # Filter by topic when detected
        if topic and topic not in chunk_topic:
            continue

        chunk_words = set(
            re.findall(r"\b[a-zA-Z]{3,}\b", chunk.lower())
        )

        score = len(question_words & chunk_words)

        if score > 0:
            scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda item: item[0], reverse=True)

    return [chunk for score, chunk in scored_chunks[:5]]


# 5. Format answer into up to 5 points
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

    points = points[:5]

    return "\n".join(
        f"{i}. {point}"
        for i, point in enumerate(points, start=1)
    )


# 6. Main chatbot function
def get_answer(question):
    documents = load_documents()

    if not documents:
        return "No Karnataka information files found."

    chunks = create_chunks(documents)

    results = retrieve(question, chunks)

    answer = format_answer(results)

    return answer
