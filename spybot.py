import streamlit as st
from huggingface_hub import hf_hub_download
import joblib

# Load the phishing detection model
@st.cache_resource  # Cache the model to avoid reloading on every interaction
def load_model():
    model_path = hf_hub_download("pirocheto/phishing-url-detection", "sklearn_model.joblib")
    return joblib.load(model_path)

model = load_model()

# Streamlit App
st.title("Phishing URL Detector")
st.write("Enter a URL below to check if it is a phishing website or safe.")

# Input text box for the URL
url_input = st.text_input("Enter URL:", placeholder="e.g., http://example.com")

# Prediction logic
if st.button("Check"):
    if url_input.strip() == "":
        st.warning("Please enter a valid URL.")
    else:
        try:
            # Make prediction
            prediction = model.predict([url_input])[0]
            confidence = model.predict_proba([url_input])[0][prediction]

            # Interpret results
            label = "Phishing" if prediction == 1 else "Safe"
            confidence_percentage = confidence * 100 if prediction == 1 else (1 - confidence) * 100

            # Display results
            st.success(f"Prediction: {label}")
            st.info(f"Confidence: {confidence_percentage:.2f}%")
        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")
