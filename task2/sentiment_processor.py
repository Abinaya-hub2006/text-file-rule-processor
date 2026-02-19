"""
Dataset Loader & Processor
"""

import pandas as pd
from sentiment_rules import calculate_score, assign_sentiment


def load_and_process(csv_path, limit=10000):
    results = []

    try:
        df = pd.read_csv(csv_path)

        if "review" not in df.columns:
            raise ValueError("CSV must contain 'review' column.")

        reviews = df["review"].dropna().iloc[:limit]

        for review in reviews:
            try:
                score = calculate_score(review)
                sentiment = assign_sentiment(score)
                results.append((review, score, sentiment))

            except Exception as e:
                print("Error processing review:", e)

        return results

    except FileNotFoundError:
        print("Dataset file not found.")
        return []

    except pd.errors.EmptyDataError:
        print("CSV file is empty.")
        return []

    except Exception as e:
        print("Unexpected error:", e)
        return []
