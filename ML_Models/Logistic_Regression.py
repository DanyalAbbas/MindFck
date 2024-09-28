from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


def Train_Logistic_Regression(x,y):
    global model
    model = LogisticRegression()
    model.fit(x,y)

def Predict_Logistic_Regression(x):
    global model, predictions
    predictions = model.predict(x)

def Plot_Logistic_Regression(x,y):
    plt.figure()
    plt.scatter(x, y, label='Original Data')
    plt.plot(x, predictions, color='red', label='Model Prediction')
    plt.legend()