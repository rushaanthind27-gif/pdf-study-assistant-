import streamlit as st
import PyPDF2
import nltk
import random
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# ---------- UI ----------
st.set_page_config(page_title="PDF Study Assistant", page_icon="📘")

st.markdown("""
<style>
.card {
    background:#0f172a;
    padding:20px;
    border-radius:12px;
    margin-bottom:15px;
}
.stButton>button {
    width:100%;
    background:#2563eb;
    color:white;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.title("📘 PDF Study Assistant")
st.caption("Turn PDFs into flashcards and practice questions")

# ---------- PDF ----------
def extract_text(pdf):
    reader = PyPDF2.PdfReader(pdf)
    return " ".join(page.extract_text() or "" for page in reader.pages)

# ---------- NLP ----------
stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text

def extract_keywords(text):
    words = word_tokenize(text.lower())
    words = [w for w in words if w.isalpha() and w not in stop_words and len(w) > 4]
    freq = nltk.FreqDist(words)
    return [w for w,_ in freq.most_common(20)]

def generate_flashcards(text):
    sentences = sent_tokenize(text)
    keywords = extract_keywords(text)
    cards = []

    for sent in sentences:
        for kw in keywords:
            if kw in sent.lower():
                cards.append((kw.capitalize(), sent))
                break
        if len(cards) == 10:
            break
    return cards

def generate_blanks(text):
    sentences = sent_tokenize(text)
    keywords = extract_keywords(text)
    questions = []

    for sent in sentences:
        for kw in keywords:
            if kw in sent.lower():
                q = sent.replace(kw, "_____")
                options = random.sample(keywords, min(4,len(keywords)))
                if kw not in options:
                    options[0] = kw
                random.shuffle(options)
                questions.append((q, options, kw))
                break
        if len(questions) == 5:
            break
    return questions

# ---------- Upload ----------
pdf = st.file_uploader("Upload a PDF", type="pdf")

if pdf and st.button("Generate Study Material"):
    with st.spinner("Reading PDF..."):
        text = clean_text(extract_text(pdf))

    st.session_state.cards = generate_flashcards(text)
    st.session_state.quiz = generate_blanks(text)

# ---------- Flashcards ----------
if "cards" in st.session_state:
    st.subheader("📖 Flashcards")
    for term, definition in st.session_state.cards:
        st.markdown(f"<div class='card'><b>{term}</b><br>{definition}</div>", unsafe_allow_html=True)

# ---------- Quiz ----------
if "quiz" in st.session_state:
    st.subheader("📝 Practice Quiz")
    quiz = st.session_state.quiz

    for i,(q,options,_) in enumerate(quiz):
        st.markdown(f"<div class='card'><b>Q{i+1}.</b> {q}</div>", unsafe_allow_html=True)
        st.radio("", options, key=f"q{i}")

    if st.button("Check Answers"):
        score = 0
        for i,(_,_,ans) in enumerate(quiz):
            if st.session_state.get(f"q{i}") == ans:
                score += 1
        st.success(f"Score: {score} / {len(quiz)}")
