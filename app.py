from flask import Flask, render_template, request
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']

    # Load the trained model
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Load the fitted feature_extraction
    with open('feature_extraction.pkl', 'rb') as file:
        feature_extraction = pickle.load(file)

    input_data_features = feature_extraction.transform([text])
    prediction = model.predict(input_data_features)
    result = "Ham mail" if prediction[0] == 1 else "Spam mail"
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run()
