import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('cyber_attacks.csv')  # Replace with your actual file name

# 1. Data processing to delete some rows and columns
# Remove rows with missing values
df = df.dropna()

# Remove unnecessary columns (adjust as needed)
columns_to_drop = ['timestamp', 'source_ip', 'destination_ip']  # Example columns
df = df.drop(columns=columns_to_drop)

# 2. Find the number of attacks possible in the dataset
attack_counts = df['attack_type'].value_counts()
total_attacks = attack_counts.sum()
print(f"Total number of attacks: {total_attacks}")

# 3. How many patterns (types of attacks) are there in the dataset
num_attack_types = len(attack_counts)
print(f"Number of attack types: {num_attack_types}")

# 4. Discard attacks with minimal number of cases
min_cases_threshold = 100  # Adjust this threshold as needed
attacks_to_keep = attack_counts[attack_counts >= min_cases_threshold].index
df = df[df['attack_type'].isin(attacks_to_keep)]

# 5. Calculate percentage for each attack type and normal traffic
attack_percentages = (df['attack_type'].value_counts() / len(df)) * 100

print("Percentages for each attack type:")
print(attack_percentages)

# 6. Code to find how many numbers of each case you have in the output
case_counts = df['attack_type'].value_counts()
print("\nNumber of cases for each attack type:")
print(case_counts)

# Visualize the distribution of attack types
plt.figure(figsize=(12, 6))
case_counts.plot(kind='bar')
plt.title('Distribution of Attack Types')
plt.xlabel('Attack Type')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
