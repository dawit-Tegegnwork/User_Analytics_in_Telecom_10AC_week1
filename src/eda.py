import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load the preprocessed data
df = pd.read_csv("data/preprocessed_data.csv")

# Identify the top 10 handsets used by customers
top_handsets = df["handset_type"].value_counts().head(10)
print(top_handsets)

# Identify the top 3 handset manufacturers
handset_manufacturers = df["handset_manufacturer"].value_counts().head(3)
print(handset_manufacturers)

# Identify the top 5 handsets per top 3 handset manufacturers
for manufacturer in handset_manufacturers.index:
    top_handsets_for_manufacturer = df[df["handset_manufacturer"] == manufacturer]["handset_type"].value_counts().head(5)
    print(f"Top 5 handsets for {manufacturer}:")
    print(top_handsets_for_manufacturer)

# Aggregate per user the required information
user_data = df.groupby("user_id")[["session_duration", "download_data", "upload_data"]].agg(["sum", "count"])
user_data.columns = ["_".join(col).strip("_") for col in user_data.columns.values]
user_data.reset_index(inplace=True)

# Treat missing values and outliers
user_data = user_data.fillna(user_data.mean())

# Perform additional EDA tasks as per the challenge requirements