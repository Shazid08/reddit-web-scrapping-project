import pandas as pd
from textblob import TextBlob
from pathlib import Path


def get_sentiment(text: str) -> float:
    """
    Return sentiment polarity in range [-1.0, 1.0]
    -1.0 = very negative, 0 = neutral, 1.0 = very positive
    """
    if not isinstance(text, str) or text.strip() == "":
        return 0.0
    return TextBlob(text).sentiment.polarity


def enrich_posts(input_path: str, output_path: str):
    print(f"Reading cleaned posts from: {input_path}")
    df = pd.read_csv(input_path)

    # Add length features
    df["title_length"] = df["title_clean"].fillna("").apply(len)
    df["selftext_length"] = df["selftext_clean"].fillna("").apply(len)

    # Add sentiment features
    df["title_sentiment"] = df["title_clean"].apply(get_sentiment)
    df["selftext_sentiment"] = df["selftext_clean"].apply(get_sentiment)

    # Ensure output dir exists
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)
    print(f"Enriched posts saved to: {output_path}")

    # Show a quick preview
    print("\nPreview of enriched data:")
    print(
        df[
            [
                "title_clean",
                "selftext_clean",
                "title_length",
                "selftext_length",
                "title_sentiment",
                "selftext_sentiment",
            ]
        ].head()
    )

    # Some basic insights
    print("\nBasic stats:")
    print("Number of posts:", len(df))
    print("Average score:", df["score"].mean())
    print("Average title sentiment:", df["title_sentiment"].mean())
    print("Average body sentiment:", df["selftext_sentiment"].mean())

    # Top post by score
    top_post = df.sort_values("score", ascending=False).iloc[0]
    print("\nTop post by score:")
    print("Title:", top_post["title"])
    print("Score:", top_post["score"])
    print("Title sentiment:", top_post["title_sentiment"])


if __name__ == "__main__":
    input_file = "data/processed/sample_posts_clean.csv"
    output_file = "data/processed/sample_posts_enriched.csv"
    enrich_posts(input_file, output_file)
