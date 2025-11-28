import pandas as pd
import re
from pathlib import Path


def clean_text(text: str) -> str:
    """
    Basic text cleaning:
    - Handle NaN/None
    - Remove URLs
    - Collapse multiple spaces/newlines
    - Strip leading/trailing spaces
    """
    if pd.isna(text):
        return ""

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Replace newlines and tabs with spaces
    text = re.sub(r"[\r\n\t]+", " ", text)

    # Collapse multiple spaces into one
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def clean_posts(input_path: str, output_path: str):
    """
    Read a raw posts CSV, add cleaned text columns, and save.
    """
    print(f"Reading: {input_path}")
    df = pd.read_csv(input_path)

    # Apply cleaning to title and selftext
    df["title_clean"] = df["title"].apply(clean_text)
    df["selftext_clean"] = df["selftext"].apply(clean_text)

    # Ensure output directory exists
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)
    print(f"Cleaned posts saved to: {output_path}")
    print(df[["title", "title_clean", "selftext", "selftext_clean"]].head())


if __name__ == "__main__":
    # For now, just run on our sample file
    input_file = "data/raw/sample_posts.csv"
    output_file = "data/processed/sample_posts_clean.csv"

    clean_posts(input_file, output_file)
