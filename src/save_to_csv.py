import pandas as pd
from pathlib import Path

def save_dataframe(df, file_path):
    # Ensures directories exist
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(file_path, index=False)
    print(f"Saved: {file_path}")     
