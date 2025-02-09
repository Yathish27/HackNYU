Spam and Phishing Model Training Summary
This notebook trains two machine learning models to classify emails as spam/ham and phishing/safe using Logistic Regression with TF-IDF vectorization. 

Access to our MVP here - https://hacknyu-phishspamdetection.streamlit.app/



Key steps:
Data Preparation:

Spam dataset: Email text (column C) and labels (0 = ham, 1 = spam).

Phishing dataset: Email text and labels (0 = safe, 1 = phishing).

Model Training:

Spam Model: Trained on spam_ham_enron.csv with 98.65% accuracy.

Phishing Model: Trained on PhishingDataset.csv with 96.83% accuracy.

Email Analysis:

A combined function analyzes emails for both spam and phishing, providing:

Spam prediction and confidence.

Phishing prediction and confidence.

Overall threat level (Low, Medium, High).

Example Predictions:

Tested on sample emails (e.g., internship fair email, PayPal phishing email).

Flask API:

A Flask app is set up to analyze emails via a POST request, returning spam and phishing predictions.

Key Libraries: pandas, numpy, scikit-learn, nltk, flask.
Models: Logistic Regression with TF-IDF for text feature extraction.
Accuracy: Spam (98.65%), Phishing (96.83%).
Use Case: Detect and classify spam and phishing emails with confidence scores.
Instructions to Run the Phishing and Spam Detection App

Install Required Libraries:

bash<button><svg><path></path></svg><span>Copy code</span><span></span></button>
pip install flask pandas numpy scikit-learn nltk

Download NLTK Stopwords:
Run the following Python code:

python<button><svg><path></path></svg><span>Copy code</span><span></span></button>
import nltk
nltk.download("stopwords")

Prepare Your Datasets:
Place PhishingDataset.csv and spam_ham_enron.csv in the project directory.

Run the Application:
Execute this command:

bash<button><svg><path></path></svg><span>Copy code</span><span></span></button>
python app.py

Access the Application:
Open a browser and go to [http://127.0.0.1:5000/] localhost - Working website -(https://hacknyu-phishspamdetection.streamlit.app/).

API Endpoint:
Post to the /analyze endpoint using:

json<button><svg><path></path></svg><span>Copy code</span><span></span></button>
{
  "emailText": "Your email content here"
}

Example Request in Python:
python<button><svg><path></path></svg><span>Copy code</span><span></span></button>
import requests
response = requests.post('http://127.0.0.1:5000/analyze', json={"emailText": "Check this email!"})
print(response.json())

Email Classifier API

This project features a Flask API designed to classify emails as either spam or phishing. It utilizes two distinct models: one for spam detection and another for phishing detection.

Usage
Install Dependencies: Ensure you have Python 3 along with the required libraries installed. You can install them using pip:
bash<button><svg><path></path></svg><span>Copy code</span><span></span></button>
pip install pandas scikit-learn flask nltk

Prepare Datasets: Place the spam_ham_enron.csv and PhishingDataset.csv datasets in the same directory as your Python script.
Run the API: Execute the Python script to launch the API. It will be accessible at http://127.0.0.1:5000.
Send a POST request: Use the following command to send a POST request to /analyze with a JSON payload that includes the email text:
bash<button><svg><path></path></svg><span>Copy code</span><span></span></button>
curl -X POST -H "Content-Type: application/json" -d '{"emailText": "Your email text here"}' http://127.0.0.1:5000/analyze

Model Training

The code trains a Logistic Regression model employing TF-IDF vectorization for both spam and phishing detection. The models are initialized and trained when the server starts.

For pages.tsx, it is the frontend landing page using NEXT.
To run the application in development mode, make sure to install the required dependencies first, then use the following command:

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Run the Application**:
   ```bash
   npm run dev

File Overview

This project contains various files essential for building a spam and phishing detection system using machine learning and browser extension technologies.

Model_Test.ipynb: A Jupyter Notebook for testing and evaluating the performance of the trained machine learning models. It helps validate the accuracy and effectiveness of the models against a test dataset.

Spam-and-Phishing-Model-Training.ipynb: This Jupyter Notebook is responsible for training the spam and phishing detection models. It contains the necessary code to preprocess data and apply machine learning algorithms, crucial for building functional models.

background.js: A background script that manages events and performs tasks without a user interface in a web extension. It plays a vital role in maintaining the extension's processes and functions.

content.js: A content script that interacts directly with web pages, gathering data and enabling user interactions. It is significant for fetching and processing email content in real-time.

manifest.json: The configuration file for the web extension. It defines the extension's metadata, scripts, and permissions, serving as the foundation for how the extension operates.

phish_model.pkl: A serialized model for phishing detection. It allows the application to load the trained model without needing to retrain, enabling faster and efficient processing during analysis.

phish_vectorizer.pkl: A serialized vectorizer for converting raw text into a numerical format suitable for the phishing model. Essential for transforming input data for model predictions.

popup.html: The HTML file that defines the user interface of the extension's popup. It allows users to interact with the features and functionalities of the extension.

popup.js: This JavaScript file controls the behavior of the popup interface, handling user events and interactions effectively.

requirements.txt: A text file that lists the necessary Python dependencies for the project. It is critical for replicating the environment and ensuring all required libraries are installed.

run.sh: A shell script that automates the execution of required processes, simplifying the running of models and APIs.

spam_model.pkl: A serialized spam detection model, allowing for quick loading and use of the trained spam classifier in analysis tasks.

spam_vectorizer.pkl: A vectorizer used for spam detection, converting text data into a numerical format for the model, crucial for effective classification.

spybot.py: A Python script that may include various functionalities related to email analysis, enriched with methods for detecting spam and phishing.

spyphish.py: Another Python script focused on phishing detection, complementing the overall functionality of the email classification system.

These files collectively enable a robust system for detecting spam and phishing threats, integrating machine learning models and web technologies for practical use.

