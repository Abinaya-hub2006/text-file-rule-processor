# task4/rules.py

POSITIVE = ["excellent", "amazing", "great", "fantastic", "love"]
NEGATIVE = ["worst", "terrible", "bad", "awful", "hate"]


def analyze_text(chunk):
    score = 0
    matched_rules = []

    text = chunk.lower()

    for word in POSITIVE:
        if word in text:
            score += 3
            matched_rules.append(word)

    for word in NEGATIVE:
        if word in text:
            score -= 3
            matched_rules.append(word)

    if score > 2:
        sentiment = "Positive"
    elif score < -2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return score, sentiment, ", ".join(matched_rules)