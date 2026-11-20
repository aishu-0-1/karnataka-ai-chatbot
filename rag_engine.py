
import os
import re

DATA_FOLDER = "data"

DISTRICTS = [
    "Bagalkote", "Ballari", "Belagavi", "Bengaluru Rural",
    "Bengaluru Urban", "Bengaluru South", "Bidar", "Chamarajanagar",
    "Chikkaballapur", "Chikkamagaluru", "Chitradurga",
    "Dakshina Kannada", "Davanagere", "Dharwad", "Gadag", "Hassan",
    "Haveri", "Kalaburagi", "Kodagu", "Kolar", "Koppal", "Mandya",
    "Mysuru", "Raichur", "Shivamogga", "Tumakuru", "Udupi",
    "Uttara Kannada", "Vijayapura", "Vijayanagara", "Yadgir"
]

TOPIC_FILES = {
    "history": "history.txt",
    "geography": "geography.txt",
    "culture": "culture_tourism.txt",
    "economy": "economy_development.txt"
}

TOPIC_NAMES = {
    "history": "History and Heritage",
    "geography": "Geography and Natural Resources",
    "culture": "Culture and Tourism",
    "economy": "Economy and Development"
}


def detect_district(question):
    q = question.lower()

    # Check longer district names first
    for district in sorted(DISTRICTS, key=len, reverse=True):
        if district.lower() in q:
            return district

    # Ramanagara is also known as Bengaluru South district
    if "ramanagara" in q:
        return "Bengaluru South"

    return None


def detect_topic(question):
    q = question.lower()

    if any(word in q for word in [
        "history", "historical", "heritage", "dynasty", "ruler"
    ]):
        return "history"

    if any(word in q for word in [
        "geography", "river", "mountain", "soil", "climate",
        natural resource", "resources"
    ]):
        return "geography"

    if any(word in q for word in [
        "culture", "tourism", "tourist", "festival",
        temple", "food", "tradition"
    ]):
        return "culture"

    if any(word in q for word in [
        "economy", "development", "industry", "agriculture",
        "business", "employment", "economic"
    ]):
        return "economy"

    return None


def read_file(file_path):
    if not os.path.exists(file_path):
        return ""

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def normalize(text):
    return re.sub(r"[^a-z]", "", text.lower())


def parse_district_sections(content):
    sections = {}
    current_district = None

    for line in content.splitlines():
        line = line.strip()

        if not line:
            continue

        # Identify district heading
        cleaned = re.sub(r"^DISTRICT\s*:\s*", "", line, flags=re.I)
        cleaned = cleaned.rstrip(":").strip()

        matched_district = None

        for district in DISTRICTS:
            if normalize(cleaned) == normalize(district):
                matched_district = district
                break

        if matched_district:
            current_district = matched_district
            sections[current_district] = []
            continue

        # Collect numbered points
        if current_district:
            point_match = re.match(
                r"^\s*(?:\d+[\.\)]|[-*])\s*(.+)$", line
            )

            if point_match:
                point = point_match.group(1).strip()
                if point:
                    sections[current_district].append(point)

    return sections


def load_base():
    database = {}

    for topic, filename in TOPIC_FILES.items():
        file_path = os.path.join(DATA_FOLDER, filename)
        content = read_file(file_path)
        database[topic] = parse_district_sections(content)

    return database


def retrieve(database, district, topic):
    if topic not in database:
        return []

    district_data = database[topic].get(district, [])
    return district_data


def get_answer(question):
    district = detect_district(question)
    topic = detect_topic(question)

    if not district:
        return (
            "Please mention a Karnataka district name in your question. "
            "Example: Explain Dharwad history."
        )

    if not topic:
        return (
            "Please mention a topic: History, Geography, "
            "Culture and Tourism, or Economy and Development."
        )

    database = load_base()
    points = retrieve(database, district, topic)

    if not points:
        return (
            f"Information Missing: I could not find {topic} information "
            f"for {district} in the document."
        )

    answer = f"DISTRICT: {district}\n"
    answer += f"TOPIC: {TOPIC_NAMES[topic]}\n\n"

    for i, point in enumerate(points[:4], start=1):
        answer += f"{i}. {point}\n"

    return answer
