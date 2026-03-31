import re
# List of suspicious keywords
suspicious_words = [
    "urgent", "immediately", "verify your account",
    "click here", "login now", "password", "bank",
    "limited time", "offer", "winner", "free", "update"
]
def check_suspicious_words(email_text):
    count = 0
    for word in suspicious_words:
        if word.lower() in email_text.lower():
            count += 1
    return count
def check_links(email_text):
    # Find URLs
    links = re.findall(r'(https?://\S+)', email_text)
    suspicious_links = 0
    for link in links:
        if "@" in link or "-" in link or "bit.ly" in link:
            suspicious_links += 1
    return suspicious_links, links
def detect_phishing(email_text):
    score = 0
    # Check suspicious words
    word_score = check_suspicious_words(email_text)
    score += word_score
    # Check links
    link_score, links = check_links(email_text)
    score += link_score * 2
    # Check for excessive uppercase
    if email_text.isupper():
        score += 2
    # Final result
    if score >= 5:
        result = "High Risk: Likely Phishing Email"
    elif score >= 3:
        result = "Medium Risk: Suspicious Email"
    else:
        result = "Low Risk: Seems Safe"
    return result, score, links
print("📧 Fake Email Detector")
email_input = input("Paste your email content:\n")
result, score, links = detect_phishing(email_input)
print("\n Analysis Result:")
print("Risk Level:", result)
print("Score:", score)
if links:
    print("Links Found:")
    for link in links:
        print("-", link)
