import pandas as pd
import pickle
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv('corvus_training_data.csv')
X = df['prompt'].tolist()
y = df['aligned'].tolist()

# Same split as training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=13, random_state=42
)

# Load model
with open('corvus_classifier.pkl', 'rb') as f:
    data = pickle.load(f)
    vectorizer = data['vectorizer']
    classifier = data['classifier']

# Get predictions on test set
X_test_vec = vectorizer.transform(X_test)
y_pred = classifier.predict(X_test_vec)

# Show errors
print("="*60)
print("🔍 MISLABELED TEST SAMPLES")
print("="*60 + "\n")

errors = []
for i, (prompt, true, pred) in enumerate(zip(X_test, y_test, y_pred)):
    if true != pred:
        errors.append((prompt, true, pred))

if errors:
    print(f"Found {len(errors)} mislabeled samples:\n")
    for prompt, true, pred in errors:
        true_label = "ALIGNED" if true else "UNALIGNED"
        pred_label = "ALIGNED" if pred else "UNALIGNED"
        print(f"Prompt: {prompt}")
        print(f"  True:      {true_label}")
        print(f"  Predicted: {pred_label}")
        print()
else:
    print("✅ No errors found!")

print("="*60)
