import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Memuat model KNN dari file pickle
with open("knn_model.pkl", "rb") as file:
    knn_model = pickle.load(file)

# Memuat vektorizer dari file pickle
with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

# Fungsi untuk melakukan sentimen analisis
def analyze_sentiment(text):
    # Mengubah teks menjadi vektor fitur
    text_vectorized = vectorizer.transform([text])
    # Melakukan prediksi sentimen menggunakan model KNN
    sentiment = knn_model.predict(text_vectorized)
    if sentiment > 0:
        return "Positif"
    elif sentiment < 0:
        return "Negatif"
    else:
        return "Netral"

# Tampilan aplikasi menggunakan Streamlit
st.title("Sentimen Analisis dengan KNN")
text_input = st.text_input("Masukkan teks:")
if st.button("Analisis"):
    if text_input.strip() != "":
        sentiment = analyze_sentiment(text_input)
        st.write("Hasil Analisis Sentimen:", sentiment)