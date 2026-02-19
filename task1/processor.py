# processor.py

import os
from rules import calculate_score

def process_files(folder_path):
    results = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            score, keywords = calculate_score(content)

            results.append({
                "filename": filename,
                "content": content,
                "score": score,
                "keywords": ", ".join(keywords)
            })

    return results
