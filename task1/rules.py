# rules.py

KEYWORD_SCORES = {
    "python": 5,
    "ai": 10,
    "machine learning": 15,
    "data": 3,
    "error": -5,
    "warning": -2
}

def calculate_score(text):
    text = text.lower()
    total_score = 0
    matched_keywords = []

    for keyword, score in KEYWORD_SCORES.items():
        if keyword in text:
            total_score += score
            matched_keywords.append(keyword)

    return total_score, matched_keywords
