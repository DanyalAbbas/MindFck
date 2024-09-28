from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn import datasets
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


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
        X = [2,4,6,4,3,4,7,5]  # Adjust according to data
        y = [2,2,6,8,3,1,6,8]       # Adjust according to data

        if model_type == 'LinearRegression':
            model = LinearRegression()
            model.fit(X, y)

        return redirect(url_for('plot_results'))

@app.route('/plot_results')
def plot_results():
    diabetes = datasets.load_diabetes()
    diabetes_X = diabetes.data[:,np.newaxis, 2]

    diabetes_X_train = diabetes_X[:-30]
    diabetes_X_test = diabetes_X[-30:]

    diabetes_Y_train = diabetes.target[:-30]
    diabetes_Y_test = diabetes.target[-30:]

    model = linear_model.LinearRegression()

    model.fit(diabetes_X_train,diabetes_Y_train)

    diabetes_y_predicted = model.predict(diabetes_X_test)
    pass

        # # Save plot to string buffer and encode
        # img = io.BytesIO()
        # plt.savefig(img, format='png')
        # img.seek(0)
        # plot_url = base64.b64encode(img.getvalue()).decode()

        # return render_template('plot.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
