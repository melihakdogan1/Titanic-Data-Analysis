import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def survival_by_sex(df):
    """
    Group the DataFrame by 'Sex' and calculate the mean survival rate.
    """
    if 'Sex' in df.columns and 'Survived' in df.columns:
        survival_rate = df.groupby('Sex')['Survived'].mean().reset_index()
        return survival_rate
    else:
        print("Required columns not found.")
        return None

def plot_survival_rate(survival_rate):
    """
    Plot a bar chart of survival rate by sex.
    """
    plt.figure(figsize=(6,4))
    sns.barplot(x='Sex', y='Survived', data=survival_rate, palette='viridis')
    plt.xlabel('Sex')
    plt.ylabel('Survival Rate')
    plt.title('Survival Rate by Sex')
    plt.ylim(0, 1)
    plt.show()

if __name__ == "__main__":
    file_path = "data/train.csv"
    df = pd.read_csv(file_path)
    
    survival_rate = survival_by_sex(df)
    if survival_rate is not None:
        print(survival_rate)
        plot_survival_rate(survival_rate)
