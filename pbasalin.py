import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Memuat model KNN dari file pickle
with open("knn_model1.pkl", "rb") as file:
    knn_model = pickle.load(file)

# Memuat vektorizer dari file pickle
with open("vectorizer1.pkl", "rb") as file:
    vectorizer = pickle.load(file)

# Fungsi untuk melakukan sentimen analisis
def analyze_sentiment(text):
    # Mengubah teks menjadi vektor fitur
    text_vectorized = vectorizer.transform([text])
    # Melakukan prediksi sentimen menggunakan model KNN
    sentiment = knn_model.predict(text_vectorized)
    return sentiment

# Tampilan aplikasi menggunakan Streamlit
st.image('timnas.jpg')
st.title("Analisis Sentimen Masyarakat terhadap Tim Nasional Indonesia pada Piala AFF 2020 Menggunakan Algoritma KNN")
text_input = st.text_input("Masukkan teks:")
if st.button("Analisis"):
    if text_input.strip() != "":
        sentiment = analyze_sentiment(text_input)
        if sentiment > 0:
            st.write("Hasil Sentimen: Positif")
        elif sentiment < 0:
            st.write("Hasil Sentimen: Negatif")
        else:
            st.write("Hasil Sentimen: Netral")
    else:
        st.write("Masukkan teks terlebih dahulu.")