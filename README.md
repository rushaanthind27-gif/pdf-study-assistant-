# 📘 PDF Study Assistant

PDF Study Assistant is an offline study tool that converts any PDF into **flashcards** and **practice quizzes** so students can learn faster and revise more effectively.

Instead of just reading PDFs, this app turns them into **active learning material**.

---

## ✨ Features

- 📄 Upload any PDF (books, notes, guides, etc.)
- 📚 Automatically creates flashcards from important content
- 📝 Generates fill-in-the-blank practice questions
- ✅ Auto-scored quiz system
- ⚡ Works completely offline (no API keys required)
- 🖥 Simple and clean Streamlit interface

---

## 🧠 How it works

1. The app extracts text from the PDF  
2. Important words are detected using NLP  
3. Key sentences become flashcards  
4. Keywords are hidden to create quiz questions  
5. Users answer the quiz and get their score  

This helps convert passive reading into active studying.

---

## 🚀 How to run the app

### 1. Install dependencies

in cmd terminal paste 
pip install streamlit PyPDF2 nltk
Then click enter

Then type :
python
Inside Python:
type
import nltk
nltk.download('punkt')
nltk.download('stopwords')
exit()
2. Run the application
download file then in file explorer on top
type cmd and paste :
python -m streamlit run app.py

📖 How to use
Click Upload PDF
Select any study PDF
Click Generate Study Material
Review the flashcards
Attempt the quiz
Click Check Answers to see your score

🎯 Why this project
Most students read PDFs passively.
This app transforms them into interactive learning tools, improving understanding and memory.

🛠 Built with
Python
Streamlit
PyPDF2
NLTK

Built for MLH Global Hack Week
