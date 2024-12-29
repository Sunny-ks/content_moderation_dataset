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



import numpy as np
from sklearn.metrics import precision_recall_fscore_support, accuracy_score

# Example Data: Replace these with your actual prediction and ground_truth matrices
# Replace with your real matrices for "predictions" and "ground_truth"
predictions = np.random.randint(0, 2, (1680, 9))  # Replace with your matrix
ground_truth = np.random.randint(0, 2, (1680, 9))  # Replace with your matrix

# Compute metrics for each label
precision, recall, f1, _ = precision_recall_fscore_support(ground_truth, predictions, average=None)

# Macro-average: Average across labels
macro_precision, macro_recall, macro_f1 = precision.mean(), recall.mean(), f1.mean()

# Micro-average: Aggregate across all labels
micro_precision, micro_recall, micro_f1, _ = precision_recall_fscore_support(
    ground_truth.flatten(), predictions.flatten(), average="micro"
)

# Overall Accuracy: Percentage of rows where all columns match
overall_accuracy = accuracy_score(ground_truth, predictions)

# Print Results
print("Macro Metrics:")
print(f"Precision: {macro_precision:.4f}, Recall: {macro_recall:.4f}, F1-Score: {macro_f1:.4f}")
print("\nMicro Metrics:")
print(f"Precision: {micro_precision:.4f}, Recall: {micro_recall:.4f}, F1-Score: {micro_f1:.4f}")
print("\nOverall Accuracy:")
print(f"Accuracy: {overall_accuracy:.4f}")

