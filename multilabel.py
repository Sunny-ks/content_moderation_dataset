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



import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

# Example DataFrames: Replace these with your actual data
# Replace with your actual DataFrame
df_predictions = pd.DataFrame({
    'S': [0, 0, 1, 0],
    'H': [1, 0, 0, 0],
    'HR': [0, 0, 1, 0],
    'SH': [1, 1, 0, 0],
    'S3': [0, 0, 1, 0],
    'H2': [1, 0, 0, 0],
    'V2': [0, 1, 0, 0],
    'OK': [0, 0, 1, 0],
})

df_ground_truth = pd.DataFrame({
    'S': [0, 0, 1, 1],
    'H': [1, 0, 0, 1],
    'HR': [0, 0, 1, 0],
    'SH': [1, 0, 0, 0],
    'S3': [0, 0, 1, 0],
    'H2': [1, 0, 1, 0],
    'V2': [0, 1, 0, 0],
    'OK': [0, 0, 1, 1],
})

# Convert DataFrames to NumPy arrays
predictions = df_predictions.to_numpy()
ground_truth = df_ground_truth.to_numpy()

# Initialize dictionaries to store metrics
individual_metrics = {}

# Iterate through each label
for i, label in enumerate(df_predictions.columns):
    # Compute metrics for the current label
    precision = precision_score(ground_truth[:, i], predictions[:, i])
    recall = recall_score(ground_truth[:, i], predictions[:, i])
    f1 = f1_score(ground_truth[:, i], predictions[:, i])
    accuracy = accuracy_score(ground_truth[:, i], predictions[:, i])

    # Store metrics for the label
    individual_metrics[label] = {
        'Precision': precision,
        'Recall': recall,
        'F1-Score': f1,
        'Accuracy': accuracy
    }

# Display results
metrics_df = pd.DataFrame(individual_metrics).T
print(metrics_df)


