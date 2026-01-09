import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ----------------------------
# 1. Load dataset
# ----------------------------
df = pd.read_csv("data/raw/phishing_email.csv")

# Standardize columns
df = df[['text_combined', 'label']]
df.columns = ['text', 'label']

# ----------------------------
# 2. Vectorization (same as Day 03)
# ----------------------------
vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(df['text'])
y = df['label']

# ----------------------------
# 3. Train-test split
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------
# 4. Train models
# ----------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Naive Bayes": MultinomialNB()
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    results[name] = acc

    print("\n==============================")
    print(name)
    print("Accuracy:", acc)
    print(classification_report(y_test, y_pred))

# ----------------------------
# 5. Save best model
# ----------------------------
best_model_name = max(results, key=results.get)
best_model = models[best_model_name]

joblib.dump(best_model, "models/phishing_model.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("\nBest model saved:", best_model_name)
