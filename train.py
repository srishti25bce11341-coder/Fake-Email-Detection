import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
data = pd.read_csv("emails.csv")
data['label'] = data['label'].map({'ham': 0, 'spam': 1})
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['text'])
y = data['label']
model = LogisticRegression()
model.fit(X, y)
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
print("Model trained and saved!")
