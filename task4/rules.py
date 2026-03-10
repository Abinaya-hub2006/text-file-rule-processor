POSITIVE_WORDS = [
"excellent","amazing","great","fantastic","love","wonderful","brilliant","awesome","superb",
"outstanding","perfect","nice","good","pleasant","marvelous","spectacular","delightful",
"enjoyable","satisfying","charming","impressive","valuable","beautiful","favorable",
"magnificent","thrilling","engaging","vibrant","cheerful","lively"
]

NEGATIVE_WORDS = [
"awful","terrible","bad","worst","hate","horrible","disappointing","poor","ugly","annoying",
"boring","confusing","damaging","dangerous","defective","depressing","dirty","disturbing",
"dull","embarrassing","faulty","frustrating","gross","harmful","hostile","inferior"
]

import re

def analyze_text(chunk):

    score = 0
    matched = []

    text = re.sub(r'[^\w\s]', '', chunk.lower())

    for word in POSITIVE_WORDS:
        if word in text:
            score += 2
            matched.append(word)

    for word in NEGATIVE_WORDS:
        if word in text:
            score -= 2
            matched.append(word)

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return score, sentiment, ", ".join(matched)