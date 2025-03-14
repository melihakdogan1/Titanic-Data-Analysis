import pandas as pd

def load_data(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    """
    Example cleaning:
    - Drop rows with missing 'Age' or 'Fare'
    - Drop 'Cabin' column (too many missing values in Titanic dataset)
    """
    if 'Cabin' in df.columns:
        df = df.drop(columns = ['Cabin'])
    
    df = df.dropna(subset = ['Age', 'Fare'])
    return df

def standardize_data(df,columns):
    """
    Standardize specified columns using z-score.
    """

    for col in columns:
        mean_val = df[col].mean()
        std_val = df[col].std()
        df[col] = (df[col] - mean_val) / std_val
    return df

if __name__ == "__main__":
    file_path = "data/train.csv"
    df = load_data(file_path)
    df = clean_data(df)
    df = standardize_data(df, ['Age', 'Fare'])
    print(df.head())
    print("\nDataFrame Info:")
    print(df.info())

