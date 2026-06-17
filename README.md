# 🚫📩 Spam Ham Message Classification Dashboard

## 📌 Overview

An AI-powered Spam Detection Web Application built with Flask, Machine Learning, and NLP that classifies messages as **Spam** or **Ham (Not Spam)** in real-time. The project helps users identify unwanted messages instantly using a trained text classification model and an intuitive web interface.

---

## ✨ Features

✅ Real-Time Spam Detection

✅ Classify Messages as Spam or Ham

✅ Natural Language Processing (NLP)

✅ Text Preprocessing & Cleaning

✅ Machine Learning-Based Prediction

✅ User-Friendly Web Interface

✅ Fast and Accurate Results

✅ Responsive Design

✅ Lightweight Flask Application

✅ Easy Deployment

---

## 🛠️ Tech Stack

### Backend

🐍 Python

🌐 Flask

📊 Pandas

🔢 NumPy

🤖 Scikit-Learn

### Machine Learning

🧠 Multinomial Naive Bayes

📝 TF-IDF Vectorization

🔤 NLP Text Processing

### Frontend

🎨 HTML5

💎 CSS3

⚡ Jinja2 Templates

---

## 📂 Project Structure

```bash
spam_ham_flask/
│
├── app.py
│
├── model.pkl
│
├── vectorizer.pkl
│
├── spam.csv
│
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── css/
│   │   └── style.css
│
└── README.md
```

---

# 🎯 Key Functionalities

## 📩 Message Classification

Enter any SMS, email, or text message and instantly determine whether it is Spam or Ham.

### Example

**Input:**

```text
Congratulations! You have won ₹50,000. Click here to claim now.
```

**Output:**

```text
🚫 Spam Message
```

---

## 🔤 NLP Text Processing

The application performs:

✔ Text Cleaning

✔ Lowercase Conversion

✔ Stopword Removal

✔ Tokenization

✔ Vectorization using TF-IDF

---

## 🤖 Machine Learning Prediction

The trained model analyzes text patterns and predicts:

📩 Ham Message

🚫 Spam Message

with high accuracy.

---

# 📊 Model Pipeline

```text
Raw Message
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Machine Learning Model
      │
      ▼
Spam / Ham Prediction
```

---

# 📈 Visual Analytics Included

📊 Spam vs Ham Distribution

📩 Message Frequency Analysis

🔤 Word Frequency Analysis

☁️ Spam Word Cloud

☁️ Ham Word Cloud

📈 Model Performance Metrics

---

# 🔥 Business Use Cases

✅ Email Spam Detection

✅ SMS Filtering Systems

✅ Customer Support Automation

✅ Fraudulent Message Detection

✅ Telecom Industry Solutions

✅ Cybersecurity Applications

✅ Marketing Campaign Filtering

---

# 🚀 Installation

```bash
git clone https://github.com/your-username/spam-ham-classifier.git

cd spam-ham-classifier

pip install -r requirements.txt

python app.py
```

---

# 🌐 Run Application

```bash
python app.py
```

Application will run on:

```text
http://localhost:5000
```

---

# 📊 Dataset Information

The project uses the SMS Spam Collection Dataset containing:

📩 SMS Messages

🚫 Spam Labels

✅ Ham Labels

📝 Text Content

📈 Thousands of Real-World Messages

---

# 🎨 Dashboard Highlights

✨ Clean User Interface

⚡ Instant Predictions

🤖 AI-Powered Classification

📱 Responsive Design

🔒 Lightweight & Fast

---

# 🔮 Future Improvements

🔹 Deep Learning-Based Spam Detection

🔹 Multi-Language Support

🔹 Email Spam Classification

🔹 User Authentication System

🔹 Message History Tracking

🔹 REST API Integration

🔹 Real-Time Prediction Analytics

🔹 Power BI Dashboard Integration

---

# 👨‍💻 Author

**Mukul Kumawat**

📧 [mukulkumawat449@gmail.com](mailto:mukulkumawat449@gmail.com)

🔗 LinkedIn: [https://www.linkedin.com/in/mukul-kumawat-6b998424b](https://www.linkedin.com/in/mukul-kumawat-6b998424b)

🔗 GitHub: [https://github.com/](https://github.com/)

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub and sharing it with others.

**Made with ❤️ using Python, Flask, Machine Learning, and NLP.** 🚀
