import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

# ── Load Cleaned Data ─────────────────────────────────────────────────────────

print("Loading cleaned data...")
df = pd.read_csv(r'C:\Users\lenovo\Desktop\Social_Lens\data\cleaned_tweets.csv')

# Drop empty rows
df = df.dropna(subset=['cleaned_text'])
df = df[df['cleaned_text'].str.strip() != '']

print(f"Dataset size: {len(df)} tweets")

# ── Features and Labels ───────────────────────────────────────────────────────

X = df['cleaned_text']
y = df['sentiment']

# ── Train/Test Split ──────────────────────────────────────────────────────────

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print(f"Training: {len(X_train)} | Testing: {len(X_test)}")

# ── TF-IDF Vectorization ──────────────────────────────────────────────────────

print("\nApplying TF-IDF...")
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf  = vectorizer.transform(X_test)

print(f"Vocabulary size: {len(vectorizer.vocabulary_)}")

# ── Train Naive Bayes ─────────────────────────────────────────────────────────

print("\nTraining Naive Bayes...")
nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)
nb_preds    = nb_model.predict(X_test_tfidf)
nb_accuracy = accuracy_score(y_test, nb_preds)
print(f"Naive Bayes Accuracy: {round(nb_accuracy * 100, 2)}%")

# ── Train Logistic Regression ─────────────────────────────────────────────────

print("\nTraining Logistic Regression...")
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train_tfidf, y_train)
lr_preds    = lr_model.predict(X_test_tfidf)
lr_accuracy = accuracy_score(y_test, lr_preds)
print(f"Logistic Regression Accuracy: {round(lr_accuracy * 100, 2)}%")

# ── Detailed Report ───────────────────────────────────────────────────────────

print("\n" + "="*50)
print("CLASSIFICATION REPORT — LOGISTIC REGRESSION")
print("="*50)
print(classification_report(y_test, lr_preds,
      target_names=['Negative', 'Positive']))

# ── Confusion Matrix ──────────────────────────────────────────────────────────

os.makedirs(r'C:\Users\lenovo\Desktop\Social_Lens\models', exist_ok=True)

cm = confusion_matrix(y_test, lr_preds)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Negative', 'Positive'],
            yticklabels=['Negative', 'Positive'])
plt.title('Confusion Matrix — Logistic Regression')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.tight_layout()
plt.savefig(r'C:\Users\lenovo\Desktop\Social_Lens\models\confusion_matrix.png')
print("\nConfusion matrix saved!")

# ── Save Model and Vectorizer ─────────────────────────────────────────────────

with open(r'C:\Users\lenovo\Desktop\Social_Lens\models\sentiment_model.pkl', 'wb') as f:
    pickle.dump(lr_model, f)

with open(r'C:\Users\lenovo\Desktop\Social_Lens\models\tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Model saved to models/sentiment_model.pkl")
print("Vectorizer saved to models/tfidf_vectorizer.pkl")

# ── Live Prediction Test ──────────────────────────────────────────────────────

print("\n" + "="*50)
print("LIVE PREDICTION TEST")
print("="*50)

def predict_sentiment(text):
    import re
    from nltk.stem import PorterStemmer
    from nltk.corpus import stopwords
    import nltk
    nltk.download('stopwords', quiet=True)

    stemmer   = PorterStemmer()
    stop_words = set(stopwords.words('english'))

    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r"n't\b", ' not', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.strip()
    words = [stemmer.stem(w) for w in text.split() if w not in stop_words]
    cleaned = ' '.join(words)

    vector      = vectorizer.transform([cleaned])
    prediction  = lr_model.predict(vector)[0]
    probability = lr_model.predict_proba(vector)[0]
    confidence  = round(max(probability) * 100, 2)
    label       = "POSITIVE 😊" if prediction == 1 else "NEGATIVE 😞"

    print(f"Tweet:      {text[:60]}")
    print(f"Prediction: {label} | Confidence: {confidence}%")
    print()

predict_sentiment("I love this so much, it's absolutely amazing!")
predict_sentiment("This is the worst experience I have ever had")
predict_sentiment("Just had lunch today")
