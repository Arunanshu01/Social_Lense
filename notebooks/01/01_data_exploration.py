import pandas as pd
import re
import nltk
from nltk.corpus import stopwords4457
from nltk.stem import PorterStemmer
import time

# ── Setup ────────────────────────────────────────────────────────────────────

nltk.download('stopwords', quiet=True)
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

# ── Preprocessing Function ───────────────────────────────────────────────────

def clean_tweet(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)       # remove URLs
    text = re.sub(r'@\w+', '', text)                  # remove mentions
    text = re.sub(r'#', '', text)                     # remove hashtag symbol
    text = re.sub(r"'s\b", '', text)                  # john's → john
    text = re.sub(r"n't\b", ' not', text)             # can't → can not
    text = re.sub(r"'re\b", ' are', text)             # they're → they are
    text = re.sub(r"'ve\b", ' have', text)            # i've → i have
    text = re.sub(r"'ll\b", ' will', text)            # i'll → i will
    text = re.sub(r'[^a-zA-Z\s]', '', text)           # remove punctuation/numbers
    text = text.strip()
    words = text.split()
    words = [stemmer.stem(w) for w in words if w not in stop_words]
    return ' '.join(words)

# ── Load Dataset ─────────────────────────────────────────────────────────────

print("Loading dataset...")

columns = ['sentiment', 'tweet_id', 'date', 'query', 'username', 'text']

df = pd.read_csv(
    r'C:\Users\lenovo\Desktop\Social_Lens\data\training.1600000.processed.noemoticon.csv',
    encoding='latin-1',
    names=columns
)

# ── Fix Sentiment Labels ──────────────────────────────────────────────────────

# Convert sentiment from 0/4 to 0/1
# 0 = negative (stays 0)
# 4 = positive (becomes 1)
df['sentiment'] = df['sentiment'].replace(4, 1)

print("Sentiment after fix:")
print(df['sentiment'].value_counts())

# ── Take a Sample for Development ────────────────────────────────────────────

# We use 10,000 tweets during development — 5000 positive, 5000 negative
# This keeps our iteration fast while still being representative

sample_neg = df[df['sentiment'] == 0].sample(5000, random_state=42)
sample_pos = df[df['sentiment'] == 1].sample(5000, random_state=42)

# Combine and shuffle
sample_df = pd.concat([sample_neg, sample_pos])
sample_df = sample_df.sample(frac=1, random_state=42).reset_index(drop=True)

print(f"\nSample size: {len(sample_df)} tweets")
print(f"Sentiment distribution:\n{sample_df['sentiment'].value_counts()}")

# ── Apply Preprocessing ───────────────────────────────────────────────────────

print("\nCleaning tweets... (this will take ~30 seconds for 10k rows)")

start = time.time()
sample_df['cleaned_text'] = sample_df['text'].apply(clean_tweet)
end = time.time()

print(f"Done! Time taken: {round(end - start, 2)} seconds")

# ── Inspect Results ───────────────────────────────────────────────────────────

print("\nSample of original vs cleaned tweets:")
print("-" * 60)
for i in range(5):
    print(f"ORIGINAL: {sample_df['text'].iloc[i]}")
    print(f"CLEANED:  {sample_df['cleaned_text'].iloc[i]}")
    print()

# ── Remove Empty Rows ─────────────────────────────────────────────────────────

# Some tweets become empty after cleaning (e.g. a tweet that was only a URL)
before = len(sample_df)
sample_df = sample_df[sample_df['cleaned_text'].str.strip() != '']
after = len(sample_df)

print(f"Removed {before - after} empty tweets after cleaning")
print(f"Final dataset size: {after} tweets")

# ── Save Cleaned Data ─────────────────────────────────────────────────────────

sample_df[['sentiment', 'cleaned_text']].to_csv(
    r'C:\Users\lenovo\Desktop\Social_Lens\data\cleaned_tweets.csv',
    index=False
)

print("\nCleaned data saved to data/cleaned_tweets.csv")
print("You never need to run preprocessing again — just load this file.")