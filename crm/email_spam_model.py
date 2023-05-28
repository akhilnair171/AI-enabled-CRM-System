import string
from django.conf import settings
from joblib import load
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

#KNN_MODEL_FILE = settings.BASE_DIR / 'data' / 'spam_model.joblib'
#VECTORIZER_FILE = settings.BASE_DIR / 'data' / 'tfidf.joblib'

knn = load('data/spam_model.joblib')
tfidf = load('data/tfidf.joblib')

def preprocess(text):
    text ="".join([t.lower() for t in text if t not in string.punctuation])

    # tokenize
    tokens = text.split(" ") # 'color printing ==['color', 'printing']

    # filter out stopwords
    return " ".join(t for t in tokens if t not in ENGLISH_STOP_WORDS)

def predict_spam(text):
    # process each "document" (1.e. each comment)
    processed = [preprocess(t) for t in text]
    # create vectors
    vectors = tfidf.transform(processed)

    return knn.predict(vectors)
