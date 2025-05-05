import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('your_dataset.csv')  # Replace with your actual file name

def analyze_columns(df):
    # Basic information about the dataset
    print(df.info())
    
    # Summary statistics
    print(df.describe())
    
    # Count of unique values in each column
    unique_counts = df.nunique()
    print("\nUnique value counts:")
    print(unique_counts)
    
    # Percentage of missing values
    missing_percentage = (df.isnull().sum() / len(df)) * 100
    print("\nPercentage of missing values:")
    print(missing_percentage)
    
    # Correlation matrix for numerical columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    correlation_matrix = df[numeric_cols].corr()
    
    # Plot correlation heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.show()
    
    return unique_counts, missing_percentage, correlation_matrix

# Run the analysis
unique_counts, missing_percentage, correlation_matrix = analyze_columns(df)

# Identify potential columns to drop
def identify_columns_to_drop(df, unique_counts, missing_percentage, correlation_matrix):
    columns_to_drop = []
    
    # Columns with a single unique value
    single_value_cols = unique_counts[unique_counts == 1].index.tolist()
    columns_to_drop.extend(single_value_cols)
    
    # Columns with high percentage of missing values (e.g., > 90%)
    high_missing_cols = missing_percentage[missing_percentage > 90].index.tolist()
    columns_to_drop.extend(high_missing_cols)
    
    # Highly correlated columns (e.g., correlation > 0.95)
    high_correlation_pairs = np.where(np.abs(correlation_matrix) > 0.95)
    high_correlation_pairs = [(correlation_matrix.index[x], correlation_matrix.columns[y]) 
                              for x, y in zip(*high_correlation_pairs) if x != y and x < y]
    
    # For each pair, suggest dropping one (you'll need to choose based on domain knowledge)
    for pair in high_correlation_pairs:
        columns_to_drop.append(pair[1])  # Arbitrarily choosing the second column in each pair
    
    # Remove duplicates
    columns_to_drop = list(set(columns_to_drop))
    
    return columns_to_drop

potential_drops = identify_columns_to_drop(df, unique_counts, missing_percentage, correlation_matrix)
print("\nPotential columns to drop:")
print(potential_drops)

# Preview the data without the suggested columns
df_cleaned = df.drop(columns=potential_drops)
print("\nPreview of the cleaned dataset:")
print(df_cleaned.head())
print(f"\nOriginal shape: {df.shape}, New shape: {df_cleaned.shape}")
