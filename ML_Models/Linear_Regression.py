from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def Train_Linear_Regression(x,y):
    global model
    model = LinearRegression()
    model.fit(x,y)

def Predict_Linear_Regression(x):
    global model, predictions
    predictions = model.predict(x)

def Plot_Linear_Regression(x,y):
    plt.figure()
    plt.scatter(x, y, label='Original Data')
    plt.plot(x, predictions, color='red', label='Model Prediction')
    plt.legend()