import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load pre-trained models and vectorizers
@st.cache_resource
def load_models():
    with open("spam_model.pkl", "rb") as f:
        spam_model = pickle.load(f)
    with open("spam_vectorizer.pkl", "rb") as f:
        spam_vectorizer = pickle.load(f)
    with open("phish_model.pkl", "rb") as f:
        phish_model = pickle.load(f)
    with open("phish_vectorizer.pkl", "rb") as f:
        phish_vectorizer = pickle.load(f)
    return spam_model, spam_vectorizer, phish_model, phish_vectorizer

# Analyze email content for spam and phishing detection
def analyze_email(email_text, spam_model, spam_vectorizer, phish_model, phish_vectorizer):
    # Spam detection
    spam_tfidf = spam_vectorizer.transform([email_text])
    spam_prob = spam_model.predict_proba(spam_tfidf)[0][1]
    spam_label = "Spam" if spam_prob > 0.5 else "Not Spam"
    spam_confidence = round(spam_prob * 100, 2) if spam_prob > 0.5 else round((1 - spam_prob) * 100, 2)

    # Phishing detection
    phish_tfidf = phish_vectorizer.transform([email_text])
    phish_prob = phish_model.predict_proba(phish_tfidf)[0][1]
    phish_label = "Phishing" if phish_prob > 0.5 else "Safe"
    phish_confidence = round(phish_prob * 100, 2) if phish_prob > 0.5 else round((1 - phish_prob) * 100, 2)

    return {
        "spam": {"label": spam_label, "confidence": spam_confidence},
        "phishing": {"label": phish_label, "confidence": phish_confidence},
    }

# Main Streamlit app
def main():
    st.title("Email Analysis: Spam and Phishing Detection")
    
    # Load models
    st.write("Loading models...")
    try:
        spam_model, spam_vectorizer, phish_model, phish_vectorizer = load_models()
        st.success("Models loaded successfully!")
    except Exception as e:
        st.error(f"Error loading models: {str(e)}")
        return
    
    # User input
    email_text = st.text_area("Enter the email text to analyze:")
    
    if st.button("Analyze"):
        if not email_text.strip():
            st.warning("Please enter some text to analyze.")
        else:
            # Analyze the email
            results = analyze_email(email_text, spam_model, spam_vectorizer, phish_model, phish_vectorizer)
            
            # Display results
            st.subheader("Analysis Results")
            st.write(f"**Spam Analysis:** {results['spam']['label']} (Confidence: {results['spam']['confidence']}%)")
            st.write(f"**Phishing Analysis:** {results['phishing']['label']} (Confidence: {results['phishing']['confidence']}%)")

if __name__ == "__main__":
    main()
