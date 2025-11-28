import json
import pandas as pd
from save_to_csv import save_dataframe

def load_sample_posts():
    with open("data/sample_posts.json", "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = load_sample_posts()
    save_dataframe(df, "data/raw/sample_posts.csv")
    print(df.head())
