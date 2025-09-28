Project Scenario

You are building a machine learning model to predict whether a patient has breast cancer based on medical measurements of their cell nuclei.

Dataset: Breast Cancer Wisconsin Dataset

Features (inputs): Measurements like radius, texture, smoothness, area, etc. of the cells

Target (output):

0 = Malignant (cancerous)

1 = Benign (non-cancerous)

Your goal: Use these features to train a binary classification model that predicts if a tumor is malignant or benign.

Step 1: Load and explore the dataset

Load the dataset (built into scikit-learn)

Convert it into a DataFrame

Check first 5 rows to understand the data

Check for missing values

Why: You need to know what features you have and make sure there’s no missing or invalid data before training a model.

Step 2: Prepare features and target

Features (X): All the numeric measurements

Target (y): Malignant / Benign (0 or 1)

Why: ML models need X for input and y for output.

Step 3: Split into training and test sets

Use 80% of data for training, 20% for testing

This ensures your model is evaluated on unseen data

Why: Helps you check if the model generalizes well and isn’t just memorizing the data.

Step 4: Train the classification model

Start with Logistic Regression (simple and effective)

Optionally try Random Forest for comparison

Why: To see how well different models can predict cancer type.

Step 5: Evaluate the model

Use metrics like:

Accuracy → % of correct predictions

Confusion matrix → True/False Positives/Negatives

Classification report → Precision, Recall, F1-score

Why: This shows how well your model performs and where it may make mistakes.

Step 6: Optional Enhancements

Feature importance visualization (which measurements matter most)

Comparing multiple models (Logistic Regression vs Random Forest vs SVM)

Saving the model for future predictions

✅ Summary of the Project Flow

Load dataset → explore and clean

Split into X (features) and y (target)

Train-test split

Train classification model(s)

Evaluate performance

Visualize

📊 Results

Training Features Shape: (455, 30)

Testing Features Shape: (114, 30)

✅ Accuracy: 95.6%

Classification Report
Class	      Precision	Recall	F1-Score Support
0 (Benign)	0.97	0.91	0.94	   43
1 (Malignant)	0.95	0.99	0.97	   71
Overall	        0.96	0.96	0.96	   114

Confusion Matrix
[[39  4]
 [ 1 70]]


39 benign correctly predicted, 4 misclassified.

70 malignant correctly predicted, only 1 misclassified.

🏆 Key Takeaways

Logistic Regression gave high accuracy (95.6%).

The model performed very well in identifying malignant cases (only 1 false negative).

Simple to train, interpret, and deploy for real-world applications.