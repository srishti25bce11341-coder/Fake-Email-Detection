import pickle
# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
# Simple rule-based keywords
suspicious_words = ["urgent", "click", "win", "free", "password"]
def rule_check(text):
    score = 0
    for word in suspicious_words:
        if word in text.lower():
            score += 1
    return score
def predict_email(text):
    # ML prediction
    vec = vectorizer.transform([text])
    ml_pred = model.predict(vec)[0]
    # Rule score
    rule_score = rule_check(text)
    # Final decision
    if ml_pred == 1 or rule_score >= 2:
        return "Spam / Phishing Email"
    else:
        return "Safe Email"
