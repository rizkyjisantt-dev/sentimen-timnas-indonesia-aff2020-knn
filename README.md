# 🇮🇩 Sentiment Analysis of Indonesian National Football Team at AFF 2020 Using K-Nearest Neighbors Algorithm

This project is a final assignment for the Natural Language Processing (NLP) course. It aims to analyze public sentiment toward the Indonesian National Football Team's performance during the AFF Championship 2020 using the **K-Nearest Neighbors (K-NN)** classification algorithm.

## 📌 Project Overview

Public sentiment is collected through Twitter using relevant keywords related to Indonesia’s matches and the AFF 2020 tournament. The tweets are then preprocessed and classified into three sentiment categories:
- Positive
- Negative
- Neutral

## 🧪 Workflow
1. **Data Collection** – Tweets were scraped using `snscrape` with specific keywords.
2. **Text Preprocessing** – Including:
   - Case folding
   - Tokenization
   - Stopword removal
   - Stemming (using Sastrawi for Bahasa Indonesia)
3. **Feature Extraction** – Using TF-IDF vectorization.
4. **Modeling** – Sentiment classification using K-NN algorithm.
5. **Evaluation** – Based on accuracy, precision, recall, and F1-score.

## 🛠️ Technologies & Libraries
- Python 3.x
- Sastrawi (Indonesian stemmer)
- scikit-learn
- pandas, numpy
- matplotlib, seaborn
- snscrape

## 📂 Project Structure
