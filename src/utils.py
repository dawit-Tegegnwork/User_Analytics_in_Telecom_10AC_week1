import numpy as np

def handle_missing_values(df):
    # Impute missing values with the mean of the respective column
    for column in df.columns:
        df[column] = df[column].fillna(df[column].mean())
    return df

def handle_outliers(df):
    # Identify and handle outliers based on your chosen method
    # For example, you can use the Z-score method to identify and replace outliers
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        mean = df[column].mean()
        std = df[column].std()
        df[column] = np.where(np.abs(df[column] - mean) > 3 * std, mean, df[column])
    return df