# 📘 PDF Study Assistant

An offline AI-powered study tool that turns any PDF into **flashcards** and **practice quizzes** so students can learn faster and retain more.

This app converts passive reading into **active learning**.

---

## ✨ Features

- 📄 Upload any PDF (textbooks, notes, guides)
- 📚 Automatically generates flashcards from key concepts
- 📝 Creates fill-in-the-blank practice questions
- ✅ Auto-scored quiz system
- ⚡ Works completely offline (no API keys or internet required)
- 🖥 Simple and clean Streamlit interface

---

## 🧠 How it works

1. The PDF text is extracted using PyPDF2  
2. Important keywords are detected using NLP (NLTK)  
3. Key sentences become **flashcards**  
4. Keywords are hidden to create **practice questions**  
5. Users answer the quiz and get instant feedback  

This makes studying more effective than just reading.

---

## 🚀 How to run the app

### 1. Install dependencies

```bash
pip install streamlit PyPDF2 nltk
