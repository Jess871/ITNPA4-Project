# Q2.3 web interface
import re
import joblib
import nltk
import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# pahe heading
st.title("Researchly Research Abstract Classifier")
st.write("This app classifies research abstracts as either AI-related or classical research.")


# Download the NLTK data once 
@st.cache_resource
def download_nltk():
    for pkg in ["punkt", "punkt_tab", "stopwords", "wordnet"]:
        nltk.download(pkg, quiet=True)


download_nltk()

# text cleaning 
stop_words = set(stopwords.words("english"))
stop_words.update(["inflation", "paper", "also", "abstract", "purpose"])
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"copyright.*|©.*", " ", text)
    text = re.sub(r"institutional subscribers.*", " ", text)
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w not in stop_words and len(w) > 1]
    tokens = [lemmatizer.lemmatize(w) for w in tokens]
    return " ".join(tokens)


# loading model from question 2.2
@st.cache_resource
def load_model():
    return joblib.load("best_model.joblib")


saved = load_model()
model, classes = saved["model"], saved["classes"]
LABEL_NAMES = {"ai": "artificial intelligence", "classical": "classical research"}

# web interface
abstract = st.text_area("Enter research abstract:", height=200)

if st.button("Classify Abstract"):
    if not abstract.strip():
        st.warning("Please enter an abstract first.")
    else:
        prediction = model.predict([clean_text(abstract)])[0]
        label = classes[prediction]
        st.subheader("Prediction")
        st.success(f"The abstract is classified as: {LABEL_NAMES[label]}")