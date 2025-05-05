import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('your_dataset.csv')  # Replace with your actual file name

def reduce_dataset(df, target_size=150000):
    # Calculate the current distribution of attack types
    attack_distribution = df['Attack'].value_counts(normalize=True)
    
    # Calculate the number of samples to keep for each attack type
    samples_per_attack = (attack_distribution * target_size).round().astype(int)
    
    # Ensure we don't exceed the target size due to rounding
    while samples_per_attack.sum() > target_size:
        samples_per_attack[samples_per_attack.idxmax()] -= 1
    
    # Create the reduced dataset
    reduced_df = pd.DataFrame()
    for attack_type, sample_size in samples_per_attack.items():
        if sample_size > 0:
            attack_df = df[df['Attack'] == attack_type]
            sampled_attack_df = attack_df.sample(n=sample_size, random_state=42)
            reduced_df = pd.concat([reduced_df, sampled_attack_df], ignore_index=True)
    
    return reduced_df

# Reduce the dataset
reduced_df = reduce_dataset(df, target_size=150000)

# Verify the results
print(f"Original dataset shape: {df.shape}")
print(f"Reduced dataset shape: {reduced_df.shape}")
print("\nOriginal attack distribution:")
print(df['Attack'].value_counts(normalize=True))
print("\nReduced attack distribution:")
print(reduced_df['Attack'].value_counts(normalize=True))

# Save the reduced dataset
reduced_df.to_csv('reduced_dataset.csv', index=False)
print("\nReduced dataset saved as 'reduced_dataset.csv'")
