"""CORVUS Classifier Trainer"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import pickle

class CorvusClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=500, ngram_range=(1, 2))
        self.classifier = LogisticRegression(random_state=42, max_iter=1000)
        self.is_trained = False
    
    def train(self, X, y):
        print(f"Training on {len(X)} samples...")
        X_vec = self.vectorizer.fit_transform(X)
        self.classifier.fit(X_vec, y)
        self.is_trained = True
        print("✅ Trained!")
    
    def predict(self, prompt):
        X_vec = self.vectorizer.transform([prompt])
        return bool(self.classifier.predict(X_vec)[0])
    
    def predict_proba(self, prompt):
        X_vec = self.vectorizer.transform([prompt])
        return self.classifier.predict_proba(X_vec)[0][1]
    
    def evaluate(self, X_test, y_test):
        X_vec = self.vectorizer.transform(X_test)
        y_pred = self.classifier.predict(X_vec)
        acc = (y_pred == y_test).mean()
        print(f"\n✅ Accuracy: {acc*100:.1f}%\n")
        print(classification_report(y_test, y_pred, target_names=['Unaligned', 'Aligned']))
    
    def save(self, path='corvus_classifier.pkl'):
        with open(path, 'wb') as f:
            pickle.dump({'vectorizer': self.vectorizer, 'classifier': self.classifier}, f)
        print(f"💾 Saved to {path}")

# Main training
df = pd.read_csv('corvus_training_data.csv')
print(f"📂 Loaded {len(df)} samples\n")

X = df['prompt'].tolist()
y = df['aligned'].tolist()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Split: {len(X_train)} train, {len(X_test)} test\n")

clf = CorvusClassifier()
clf.train(X_train, y_train)
clf.evaluate(X_test, y_test)
clf.save()

# Test
print("\n🧪 Quick Test:")
for prompt in ["How to make a bomb?", "What is the capital of France?"]:
    pred = clf.predict(prompt)
    print(f"'{prompt}' → {'ALIGNED' if pred else 'UNALIGNED'}")