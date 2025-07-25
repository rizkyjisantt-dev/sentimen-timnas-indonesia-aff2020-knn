# Sentiment Analysis of Indonesian National Football Team at AFF 2020 Using K-Nearest Neighbors

This repository contains a sentiment analysis project focused on public opinion toward the Indonesian National Football Team during the AFF Championship 2020. The analysis is conducted using the K-Nearest Neighbors (KNN) algorithm to classify sentiments expressed on Twitter into positive, neutral, and negative categories.

## 📌 Project Background

Public sentiment on social media reflects how people perceive certain events, including sports competitions. During the AFF Cup 2020, Indonesia’s performance sparked various reactions from fans on Twitter. Understanding these sentiments can help measure public support and reaction dynamically.

## 🧪 Methodology

This project follows several key steps:

1. **Data Collection**  
   - Tweets were collected using relevant keywords and hashtags during the AFF 2020.

2. **Preprocessing**  
   - Case folding  
   - Cleansing (removing punctuation, URLs, mentions, etc.)  
   - Stopword removal  
   - Tokenization  
   - Stemming  

3. **Feature Extraction**  
   - TF-IDF (Term Frequency-Inverse Document Frequency)

4. **Modeling**  
   - Sentiment classification using the **K-Nearest Neighbors (KNN)** algorithm.

5. **Evaluation**  
   - Accuracy  
   - Confusion Matrix  
   - Precision, Recall, and F1-Score

## 🛠️ Technologies Used

- Python  
- Jupyter Notebook  
- Scikit-learn  
- Pandas  
- NLTK  
- Sastrawi

## 📊 Results

- The trained KNN model successfully classified sentiments with promising evaluation results.
- Sentiment distribution showed that [insert result summary if available, e.g., “positive sentiments dominated the conversation.”]

## 📁 Repository Structure

📦sentimen-timnas-indonesia-aff2020-knn
┣ 📂data
┃ ┗ 📄dataset_twitter_aff2020.csv
┣ 📂notebooks
┃ ┗ 📄sentiment_knn_model.ipynb
┣ 📄README.md
┗ 📄requirements.txt


## 👨‍💻 Author

- Mochammad Rizki Aji Santoso – [GitHub](https://github.com/rizkyjisantt-dev) | [LinkedIn](https://linkedin.com/in/moch-rizki)

---

📌 *This project was developed for academic purposes as part of a final assignment.*  
📣 Feedback and contributions are welcome!

