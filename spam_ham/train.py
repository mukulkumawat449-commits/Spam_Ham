# ============================================================
# train.py — Train the Spam/Ham classifier and save the model
# ============================================================
# Run this file ONCE before starting the Flask app:
#   python train.py
# It reads the CSV, cleans the text, trains the model, and saves:
#   model/spam_classifier.pkl  → the trained ML model
#   model/tfidf_vectorizer.pkl → the text-to-numbers converter
# ============================================================

import os
import re
import string
import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# ── Resolve paths relative to THIS file ─────────────────────
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
CSV_PATH  = os.path.join(BASE_DIR, "spam.csv")
MODEL_DIR = os.path.join(BASE_DIR, "model")

# ── Step 1: Load the CSV dataset ────────────────────────────
print("📂 Loading dataset...")
df = pd.read_csv(CSV_PATH, encoding="latin-1")

# Keep only the message & label columns (handle both column name styles)
if 'Messages' in df.columns and 'Result' in df.columns:
    df = df[['Messages', 'Result']]
    df.columns = ['message', 'label']
elif 'v1' in df.columns and 'v2' in df.columns:
    df = df[['v1', 'v2']]
    df.columns = ['label', 'message']
else:
    raise ValueError(f"Unexpected CSV columns: {df.columns.tolist()}")

df.dropna(inplace=True)

print(f"   Total messages loaded: {len(df)}")
print(f"   Spam count : {(df['label'] == 'spam').sum()}")
print(f"   Ham  count : {(df['label'] == 'ham').sum()}")


# ── Step 2: Clean / preprocess the text ─────────────────────
def clean_text(text):
    """Lower-case, remove punctuation & digits, strip extra spaces."""
    text = str(text).lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    return text

print("\n🧹 Cleaning text messages...")
df['clean_message'] = df['message'].apply(clean_text)


# ── Step 3: Encode labels (spam=1, ham=0) ───────────────────
df['label_encoded'] = df['label'].map({'spam': 1, 'ham': 0})
# Drop rows where label wasn't spam or ham
df.dropna(subset=['label_encoded'], inplace=True)
df['label_encoded'] = df['label_encoded'].astype(int)


# ── Step 4: Split into training and testing sets ─────────────
X = df['clean_message']
y = df['label_encoded']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"\n📊 Train size: {len(X_train)} | Test size: {len(X_test)}")


# ── Step 5: Convert text to TF-IDF numbers ──────────────────
print("\n🔢 Converting text to TF-IDF features...")
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf  = vectorizer.transform(X_test)


# ── Step 6: Train both models and pick the best one ─────────
print("\n🤖 Training models...")

nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)
nb_acc = accuracy_score(y_test, nb_model.predict(X_test_tfidf))

lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train_tfidf, y_train)
lr_acc = accuracy_score(y_test, lr_model.predict(X_test_tfidf))

print(f"   Naive Bayes Accuracy        : {nb_acc * 100:.2f}%")
print(f"   Logistic Regression Accuracy: {lr_acc * 100:.2f}%")

if lr_acc >= nb_acc:
    best_model = lr_model
    model_name = "Logistic Regression"
else:
    best_model = nb_model
    model_name = "Naive Bayes"

print(f"\n✅ Best model selected: {model_name} ({max(lr_acc, nb_acc)*100:.2f}% accuracy)")
print("\n📋 Detailed Classification Report:")
print(classification_report(
    y_test,
    best_model.predict(X_test_tfidf),
    target_names=['Ham', 'Spam']
))


# ── Step 7: Save the model and vectorizer to disk ───────────
os.makedirs(MODEL_DIR, exist_ok=True)

with open(os.path.join(MODEL_DIR, "spam_classifier.pkl"), "wb") as f:
    pickle.dump(best_model, f)

with open(os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl"), "wb") as f:
    pickle.dump(vectorizer, f)

print(f"\n💾 Model saved      → {MODEL_DIR}/spam_classifier.pkl")
print(f"💾 Vectorizer saved → {MODEL_DIR}/tfidf_vectorizer.pkl")
print("\n🎉 Training complete! Now run:  python app.py")
