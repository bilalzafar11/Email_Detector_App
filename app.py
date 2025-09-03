import sys
sys.stdout.reconfigure(encoding='utf-8')

from flask import Flask, render_template, request, flash
import joblib
import os

# ==========================
# Initialize Flask App
# ==========================
app = Flask(__name__)
app.secret_key = "super_secret_key"  # Needed for flash messages

# ==========================
# Load Trained Model & Vectorizer (Absolute Paths)
# ==========================
model, vectorizer = None, None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "spam_classifier.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "tfidf_vectorizer.pkl")

if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    try:
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        print("✅ Model & Vectorizer loaded successfully!")
    except Exception as e:
        print(f"❌ Error loading model/vectorizer: {e}")
else:
    print("❌ Model or Vectorizer file not found!")


# ==========================
# Custom Rule-Based Filter
# ==========================
def custom_filter(email_text, model_prediction):
    trusted_keywords = [
        "meezan bank", "hbl", "mcb", "ubl", "askari bank",
        "standard chartered", "linkedin", "leetcode", "payoneer"
    ]

    text_lower = email_text.lower()

    for keyword in trusted_keywords:
        if keyword in text_lower:
            return "Not Spam"

    return model_prediction


# ==========================
# Home Route
# ==========================
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probability = None
    spam_confidence = None
    notspam_confidence = None
    email_text = None

    if request.method == "POST":
        email_text = request.form.get("email", "").strip()

        if not email_text:
            flash("⚠️ Please enter email text!", "warning")
        elif not model or not vectorizer:
            flash("❌ Model not loaded properly. Please check files.", "danger")
        else:
            try:
                email_vector = vectorizer.transform([email_text])
                result = model.predict(email_vector)[0]
                proba = model.predict_proba(email_vector)[0]

                raw_prediction = "Spam" if result == 1 else "Not Spam"
                prediction = custom_filter(email_text, raw_prediction)

                spam_confidence = f"{proba[1] * 100:.2f}%"
                notspam_confidence = f"{proba[0] * 100:.2f}%"
                probability = f"{max(proba) * 100:.2f}%"

            except Exception as e:
                flash(f"❌ Error during prediction: {e}", "danger")

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability,
        spam_confidence=spam_confidence,
        notspam_confidence=notspam_confidence,
        email_text=email_text
    )


# ==========================
# Run Flask App
# ==========================
if __name__ == "__main__":
    app.run(debug=True)
