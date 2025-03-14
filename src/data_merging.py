import pandas as pd

def merge_data(df_train, df_test, on_column):
    """
    Merge two DataFrames on a specified column using an inner join.
    """
    merged_df = pd.merge(df_train, df_test, on=on_column, how="inner")
    return merged_df

if __name__ == "__main__":
    df_train = pd.read_csv("data/train.csv")
    df_test = pd.read_csv("data/test.csv")

    # Merge the train and test data on the 'PassengerId' column
    merged_df = merge_data(df_train, df_test, on_column="PassengerId")
    print(merged_df.head())
    print("Merged DataFrame shape:", merged_df.shape)
