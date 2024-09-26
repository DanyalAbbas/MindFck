from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Placeholder to store uploaded data and models
data = pd.DataFrame()
model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global data
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.xlsx'):
            data = pd.read_excel(file)
            return redirect(url_for('choose_model'))

@app.route('/choose_model')
def choose_model():
    return render_template('choose_model.html')

@app.route('/train_model', methods=['POST'])
def train_model():
    global model, data
    if request.method == 'POST':
        model_type = request.form['model']
        X = data[['feature1']].values  # Adjust according to data
        y = data['target'].values      # Adjust according to data

        if model_type == 'LinearRegression':
            model = LinearRegression()
            model.fit(X, y)

        return redirect(url_for('plot_results'))

@app.route('/plot_results')
def plot_results():
    global model, data
    if model is not None:
        # Plot data and predictions
        X = data[['feature1']].values  # Adjust according to data
        y = data['target'].values      # Adjust according to data
        predictions = model.predict(X)

        plt.figure()
        plt.scatter(X, y, label='Original Data')
        plt.plot(X, predictions, color='red', label='Model Prediction')
        plt.legend()

        # Save plot to string buffer and encode
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        return render_template('plot.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
