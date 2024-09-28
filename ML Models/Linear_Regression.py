from sklearn.linear_model import LinearRegression

def Train_Linear_Regression(x,y):
    global model
    model = LinearRegression()
    model.fit(x,y)

def Predict_Linear_Regression(x,y):
    global model
    predictions = model.predict(x)
