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
    # global data
    # if request.method == 'POST':
    #     file = request.files['file']
    #     if file and file.filename.endswith('.xlsx'):
    #         data = pd.read_excel(file)
    #         return redirect(url_for('choose_model'))
# @app.route('/upload')
# def upload_file():
    

@app.route('/choose_model')
def choose_model():
    return render_template('choose_model.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)

    # app.run(debug=True)
