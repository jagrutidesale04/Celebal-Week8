import pandas as pd

def load_loan_data(csv_path="data/Training Dataset.csv"):
    df = pd.read_csv(csv_path)
    df.fillna("Unknown", inplace=True)
    return df

def convert_to_text(df):
    records = []
    for i, row in df.iterrows():
        records.append(" | ".join(f"{col}: {val}" for col, val in row.items()))
    return records
