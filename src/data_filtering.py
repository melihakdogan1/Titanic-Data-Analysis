import pandas as pd

def filter_by_age(df, age_threshold=30):
    """
    Filter rows where the 'Age' column is greater than the specified threshold.
    """

    if 'Age' in df.columns:
        filtered_df = df[df['Age'] > age_threshold]
        return filtered_df
    else:
        print("Column 'Age' not found in DataFrame.")
        return df

def group_by_sex_and_survival(df):
    """
    Group the DataFrame by 'Sex' and calculate the mean survival rate.
    """
    if 'Sex' in df.columns and 'Survival' in df.columns:
        group = df.groupby('Sex')['Survived'].mean()
        return group
    else:
        print("Required columns not found.")
        return None
    
def filter_with_query(df, query_str):
    """
    Filter DataFrame rows using the query() method. 
    """
    try:
        filtered_df = df.query(query_str)
        return filtered_df
    except Exception as e:
        print("Error in query filtering: ", e)
        return df

if __name__ == "__main__":
    file_path = "data/train.csv"
    df = pd.read_csv(file_path)

    # Filter passengers older than 30
    df_age_filtered = filter_by_age(df, age_threshold=30)
    print("Rows where Age > 30:")
    print(df_age_filtered.head())

    # Group by gender and calculate survival rates
    survival_by_sex = group_by_sex_and_survival(df)
    print("\nSurvival rate by Sex:")
    print(survival_by_sex)

    #  Filtering using Query
    query_str = "Pclass == 1 and Age > 30"
    df_query_filtered = filter_with_query(df, query_str)
    print("\nFiltered DataFrame using query (Pclass == 1 and Age > 30):")
    print(df_query_filtered.head())

