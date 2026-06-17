import os
import pickle
import re
import string

from flask import Flask, render_template, request

# ── Create the Flask app ─────────────────────────────────────
app = Flask(__name__)

# ── Resolve paths relative to THIS file (not the CWD) ───────
# This is the #1 fix: using __file__ ensures the model loads
# correctly no matter which directory Flask/gunicorn is started from.
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR  = os.path.join(BASE_DIR, "model")

# ── Load the saved model and vectorizer ─────────────────────
print("Loading model and vectorizer...")

with open(os.path.join(MODEL_DIR, "spam_classifier.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)

print("Model loaded successfully! ✅")


# ── Helper: clean text (same logic as in train.py) ──────────
def clean_text(text):
    """Apply the same cleaning we did during training."""
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    return text


# ── Route 1: Home page ───────────────────────────────────────
@app.route("/")
def home():
    return render_template("index.html")


# ── Route 2: Predict endpoint ────────────────────────────────
@app.route("/predict", methods=["POST"])
def predict():
    user_message = request.form.get("message", "").strip()

    if not user_message:
        return render_template(
            "index.html",
            error="⚠️ Please enter a message before clicking Check!"
        )

    cleaned          = clean_text(user_message)
    message_vector   = vectorizer.transform([cleaned])
    prediction       = model.predict(message_vector)[0]
    probabilities    = model.predict_proba(message_vector)[0]
    confidence       = round(probabilities[prediction] * 100, 2)
    result_label     = "Spam 🚫" if prediction == 1 else "Ham ✅"
    result_type      = "spam"   if prediction == 1 else "ham"

    return render_template(
        "index.html",
        original_message=user_message,
        result_label=result_label,
        result_type=result_type,
        confidence=confidence,
        show_result=True
    )


# ── Start the Flask development server ───────────────────────
if __name__ == "__main__":
    # Read PORT from environment (required by Render, Railway, Heroku, etc.)
    # Falls back to 5000 for local development
    port  = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
