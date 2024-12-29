import pandas as pd

# Load your dataset
# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('your_file.csv')

# Define the possible labels
labels = ['S', 'SH', 'V', 'H', 'HR', 'H2', 'V2', 'OK']

# Convert 'response' column to multi-label binary matrix
for label in labels:
    df[label] = df['response'].apply(lambda x: 1 if label in str(x).split(',') else 0)

# Verify the conversion
print(df.head())

# Save the updated dataframe with the multi-label columns
df.to_csv('multi_label_dataset.csv', index=False)
