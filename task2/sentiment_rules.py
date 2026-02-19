"""
Rule-based Sentiment Scoring System
"""

POSITIVE_KEYWORDS = {
    "excellent": 5,
    "amazing": 4,
    "love": 4,
    "great": 3,
    "fantastic": 5,
    "wonderful": 4,
    "best": 4,
    "awesome": 4,
    "brilliant": 4,
    "superb": 4
}

NEGATIVE_KEYWORDS = {
    "worst": -5,
    "terrible": -5,
    "bad": -3,
    "boring": -3,
    "awful": -5,
    "disappointing": -4,
    "poor": -3,
    "hate": -4,
    "waste": -4,
    "pathetic": -4
}


def calculate_score(text):
    score = 0
    text = text.lower()

    for word, value in POSITIVE_KEYWORDS.items():
        if word in text:
            score += value

    for word, value in NEGATIVE_KEYWORDS.items():
        if word in text:
            score += value

    return score


def assign_sentiment(score):
    if score > 3:
        return "Positive"
    elif score < -3:
        return "Negative"
    else:
        return "Neutral"
