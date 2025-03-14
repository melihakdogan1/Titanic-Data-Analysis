import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_age_distribution(df):
    """
    Plot a histogram to display the distribution of passenger ages.
    """
    plt.figure(figsize=(8,6))
    if 'Age' in df.columns:
        sns.histplot(df['Age'], bins=20, color='skyblue')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.title('Age Distribution')
        plt.show()
    else:
        print("Column 'Age' not found in DataFrame.")

if __name__ == "__main__":
    file_path = "data/train.csv" # Read Train CSV file
    df = pd.read_csv(file_path)

    visualize_age_distribution(df)
