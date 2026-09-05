import re 
import nltk 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#download required nltk data (only needed once)
nltk.download('stopwords')

#initialize the stemmer
stemmer = PorterStemmer()

#load english Stopwords.
stop_words = set(stopwords.words('english'))

def clean_tweet(text):
    
    # Step 1: Convert to lowercase
    text = text.lower()

    # Step 2: Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Step 3: Remove @mentions
    text = re.sub(r'@\w+', '', text)

    # Step 4: Remove hashtag symbol but keep the word
    text = re.sub(r'#', '', text)

    # Step 5: Replace apostrophes before removing punctuation
    # This ensures "that's" → "thats" → then we catch contractions
    # Better: expand contractions so "that's" → "that is"
    text = re.sub(r"'s\b", '', text)      # remove possessives: "john's" → "john"
    text = re.sub(r"n't\b", ' not', text) # expand: "can't" → "can not"
    text = re.sub(r"'re\b", ' are', text) # expand: "they're" → "they are"
    text = re.sub(r"'ve\b", ' have', text)# expand: "i've" → "i have"
    text = re.sub(r"'ll\b", ' will', text)# expand: "i'll" → "i will"

    # Step 6: Remove all remaining punctuation and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Step 7: Remove extra whitespace
    text = text.strip()

    # Step 8: Tokenize — split into words
    words = text.split()

    # Step 9: Remove stopwords and stem
    words = [stemmer.stem(word) for word in words if word not in stop_words]

    # Step 10: Join back into string
    return ' '.join(words)

test_tweets = [
    "@switchfoot http://twitpic.com/2y1zl - Awww, that's a bummer!!",
    "I LOVE this product!! So happy :)",
    "@john check out www.example.com this is amazing #love",
    "I can't believe they're doing this, it's not right!",
    "She's the best person I've ever met, I'll miss her"
]

for tweet in test_tweets:
    print("ORIGINAL:", tweet)
    print("CLEANED: ", clean_tweet(tweet))
    print()

    # Debug: check if 'that' is in our stopwords
print("Is 'that' in stopwords?", 'that' in stop_words)
print("Is 'love' in stopwords?", 'love' in stop_words)