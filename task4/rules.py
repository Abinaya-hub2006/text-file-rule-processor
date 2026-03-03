# task4/rules.py

POSITIVE = ["excellent", "amazing", "great", "fantastic", "love", "wonderful"]
NEGATIVE = ["worst", "terrible", "bad", "awful", "hate", "boring"]


def calculate_score(text):
    score = 0
    text = text.lower()

    for word in POSITIVE:
        if word in text:
            score += 3

    for word in NEGATIVE:
        if word in text:
            score -= 3

    return score


def assign_sentiment(score):
    if score > 2:
        return "Positive"
    elif score < -2:
        return "Negative"
    else:
        return "Neutral"