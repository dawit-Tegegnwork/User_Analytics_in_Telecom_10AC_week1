import pandas as pd
from src.database import query_db
from src.utils import handle_missing_values, handle_outliers

def fetch_data():
    query = "SELECT * FROM telecom_data;"
    rows = query_db(query)
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
    return df

def preprocess_data(df):
    df = handle_missing_values(df)
    df = handle_outliers(df)
    # Add any other data preprocessing steps here
    return df

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    raw_data = fetch_data()
    processed_data = preprocess_data(raw_data)
    save_data(processed_data, "data/processed_data.csv")