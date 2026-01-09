import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

nltk.download('stopwords')

df = pd.read_csv("data/raw/phishing_email.csv")

df = df[['text_combined', 'label']]
df.columns = ['text', 'label']

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)   
    text = re.sub(r"[^a-z\s]", "", text)         
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

df['text'] = df['text'].apply(clean_text)



vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(df['text'])
y = df['label']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Preprocessing completed!")
print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

import joblib

joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")
print("TF-IDF vectorizer saved!")
