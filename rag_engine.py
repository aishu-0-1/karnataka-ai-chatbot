import re
from pathlib import Path

# ========================================================= 
# 1. DATA FILE LOCATION
# =========================================================
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# =========================================================
# 2. DISTRICT NAMES AND ALIASES
# =========================================================
DISTRICT_ALIASES = {
    "Bagalkote": ["bagalkote", "bagalkot"],
    "Ballari": ["ballari", "bellary"],
    "Belagavi": ["belagavi", "belgaum"],
    "Bengaluru Rural": ["bengaluru rural", "bangalore rural"],
    "Bengaluru Urban": ["bengaluru urban", "bangalore urban", "bengaluru", "bangalore"],
    "Bengaluru South": ["bengaluru south", "ramanagara", "ram nagara"],
    "Bidar": ["bidar"],
    "Chamarajanagar": ["chamarajanagar", "chamaraja nagar"],
    "Chikkaballapur": ["chikkaballapur", "chikballapur"],
    "Chikkamagaluru": ["chikkamagaluru", "chikmagalur"],
    "Chitradurga": ["chitradurga"],
    "Dakshina Kannada": ["dakshina kannada", "south kannara", "mangalore district"],
    "Davanagere": ["davanagere", "davangere"],
    "Dharwad": ["dharwad"],
    "Gadag": ["gadag"],
    "Hassan": ["hassan"],
    "Haveri": ["haveri"],
    "Kalaburagi": ["kalaburagi", "gulbarga"],
    "Kodagu": ["kodagu", "coorg"],
    "Kolar": ["kolar"],
    "Koppal": ["koppal"],
    "Mandya": ["mandya"],
    "Mysuru": ["mysuru", "mysore"],
    "Raichur": ["raichur"],
    "Shivamogga": ["shivamogga", "shimoga"],
    "Tumakuru": ["tumakuru", "tumkur", "tummkur", "tummkruu", "tummkru", "tumkru"],
    "Udupi": ["udupi"],
    "Uttara Kannada": ["uttara kannada", "north kannara", "karwar district"],
    "Vijayapura": ["vijayapura", "bijapur"],
    "Vijayanagara": ["vijayanagara", "vijayanagaram"],
    "Yadgir": ["yadgir", "yadagiri"],
}

# =========================================================
# 3. TOPIC FILES
# =========================================================
TOPIC_FILES = {
    "history": "history.txt",
    "geography": "geography.txt",
    "culture": "culture_tourism.txt",
    "economy": "economy_development.txt",
}

TOPIC_KEYWORDS = {
    "history": [
        "history", "historical", "heritage", "dynasty",
        "fort", "king", "ancient", "empire"
    ],
    "geography": [
        "geography", "river", "rivers", "climate", "soil",
        "mountain", "hill", "natural resource", "resources"
    ],
    "culture": [
        "culture", "tourism", "tourist", "festival",
        "food", "tradition", "temple", "places to visit"
    ],
    "economy": [
        "economy", "economic", "development", "industry",
        "industries", "agriculture", "business", "employment"
    ],
}

# =========================================================
# 4. DISTRICT DETECTION
# =========================================================
def detect_district(question):
    q = question.lower()

    # Match longer aliases first
    aliases_sorted = sorted(
        [
            (district, alias)
            for district, aliases in DISTRICT_ALIASES.items()
            for alias in aliases
        ],
        key=lambda item: len(item[1]),
        reverse=True
    )

    for district, alias in aliases_sorted:
        pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"
        if re.search(pattern, q):
            return district

    return None

# =========================================================
# 5. TOPIC DETECTION
# =========================================================
def detect_topics(question):
    q = question.lower()
    found = []

    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(keyword in q for keyword in keywords):
            found.append(topic)

    # If no topic is mentioned, search all topics
    if not found:
        return list(TOPIC_FILES.keys())

    return found

# =========================================================
# 6. LOAD A TEXT FILE
# =========================================================
def load_file(filename):
    file_path = DATA_DIR / filename

    if not file_path.exists():
        return ""

    try:
        return file_path.read_text(encoding="utf-8")
    except Exception:
        return ""

# =========================================================
# 7. CLEAN DISTRICT HEADING
# =========================================================
def clean_heading(line):
    line = line.strip()

    # Remove Markdown heading marks
    line = re.sub(r"^#+\s*", "", line)

    # Remove common heading prefixes
    line = re.sub(
        r"^(DISTRICT|DISTRICT NAME)\s*:\s*",
        "",
        line,
        flags=re.IGNORECASE
    )

    # Remove trailing colon
    line = line.rstrip(":").strip()

    return line.lower()

# =========================================================
# 8. CHECK WHETHER LINE IS A DISTRICT HEADER
# =========================================================
def get_district_from_heading(line):
    cleaned = clean_heading(line)

    for district, aliases in DISTRICT_ALIASES.items():
        possible_names = [district.lower()] + aliases

        for name in possible_names:
            if cleaned == name.lower():
                return district

    return None

# =========================================================
# 9. EXTRACT DISTRICT SECTION FROM TEXT
# =========================================================
def extract_district_section(text, target_district):
    if not text:
        return ""

    lines = text.splitlines()
    sections = []
    current_district = None
    current_lines = []

    for line in lines:
        heading_district = get_district_from_heading(line)

        # New district heading found
        if heading_district:

            # Save previous section
            if current_district == target_district:
                sections.extend(current_lines)

            current_district = heading_district
            current_lines = []
            continue

        # Store lines belonging to current district
        if current_district == target_district:
            current_lines.append(line)

    # Save the last district section
    if current_district == target_district:
        sections.extend(current_lines)

    result = "\n".join(sections).strip()

    return result

# =========================================================
# 10. RETRIEVE DISTRICT INFORMATION
# =========================================================
def retrieve_district_info(district, topics):
    results = []

    for topic in topics:
        filename = TOPIC_FILES.get(topic)

        if not filename:
            continue

        text = load_file(filename)

        section = extract_district_section(text, district)

        if section:
            results.append(
                f"### {topic.title()} – {district}\n{section}"
            )

    return results

# =========================================================
# 11. FORMAT ANSWER
# =========================================================
def format_answer(district, results):
    if not results:
        return (
            f"Sorry, I couldn't find information for **{district}** "
            "in the selected knowledge files.\n\n"
            "Please check the district name or add the district's "
            "information to the data files."
        )

    answer = f"## 📍 District: {district}\n\n"

    answer += "\n\n".join(results)

    return answer

# =========================================================
# 12. MAIN CHATBOT FUNCTION
# =========================================================
def get_answer(question):
    if not question or not question.strip():
        return "Please enter a question about Karnataka."

    # Find district
    district = detect_district(question)

    if district is None:
        return (
            "Please mention a Karnataka district name.\n\n"
            "**Examples:**\n"
            "- Explain Tumakuru history\n"
            "- Explain Tumkur geography\n"
            "- Explain Bengaluru culture\n"
            "- Explain Dharwad"
        )

    # Find topic
    topics = detect_topics(question)

    # Retrieve information from topic files
    results = retrieve_district_info(district, topics)

    # Create final answer
    return format_answer(district, results)
