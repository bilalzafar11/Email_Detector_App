📧 AI-Based Spam Email Detector

An intelligent web-based Spam Email Detection system built using Machine Learning and deployed with Flask.
The system classifies emails as Spam or Not Spam (Ham) using NLP techniques and multiple ML algorithms.

🚀 Project Overview

This project uses Natural Language Processing (NLP) and supervised machine learning models to detect whether an email is spam or legitimate.

The system includes:

Data preprocessing & cleaning

Text vectorization using TF-IDF

Model training & evaluation

Web interface built with HTML, CSS, JavaScript

Backend integration using Flask

🧠 Machine Learning Pipeline
1️⃣ Data Handling

Dataset loaded using Pandas

Spam/Ham label distribution analysis

Null value handling

2️⃣ Text Preprocessing

Lowercasing

Removing punctuation, numbers, special characters

Stopwords removal (NLTK)

Lemmatization (WordNetLemmatizer)

3️⃣ Feature Engineering

TF-IDF Vectorization

Max Features: 5000

N-grams: (1,2)

4️⃣ Model Training

The following models were trained and evaluated:

Naive Bayes (MultinomialNB)

Logistic Regression

Support Vector Machine (Linear Kernel)

5️⃣ Evaluation Metrics

Accuracy

Precision

Recall

F1 Score

Confusion Matrix

Classification Report

🖥️ Web Application

The trained model is integrated with a Flask backend.

Frontend Technologies:

HTML

CSS

JavaScript

User can:

Enter email content

Click predict

Get real-time spam classification result
