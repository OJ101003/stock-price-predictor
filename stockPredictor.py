import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from stockPuller import *

class stockPredictor:
    def __init__(self, ticker = None) -> None:
        self.ticker = ticker
        self.priceOutput()

    def trainModel(self,X,y):
        steps = [
            ('scalar', StandardScaler()), # Normalizes the data which makes linear regression run faster and better
            ('poly', PolynomialFeatures(degree=2)), # Feature engineering which squares each feature and provides the model with that, which can allow it to make curvy lines. 
            ('model', Ridge(alpha=0.2, fit_intercept=True)) # Linear regression model that includes a loss function, this prevents overfitting and makes unneccessary data not able to affect the model
        ]
        ridge_pipe = Pipeline(steps) # Goes through the pipeline which makes the code look neater
        ridge_pipe.fit(X, y)
        return ridge_pipe

    def pricePredictor(self, data,features,model):
        prevHighVal = data['high'].iloc[0] # Previous high price of the day
        prevLowVal = data['low'].iloc[0] # Previous low price of the day
        prevOpenVal = data['open'].iloc[0] # Previous open price of the day
        data = data.dropna(axis=0)
        prevCloseVal = data['Previous Close'].iloc[0] # Previous closing price of the day
        stockTest = {"Previous Close": prevCloseVal, "high": prevHighVal, "low": prevLowVal, "open": prevOpenVal}
        test_data = pd.DataFrame(stockTest, index=[0])
        X_test = pd.get_dummies(test_data[features])
        return model.predict(X_test)[0],prevCloseVal

    def priceOutput(self):
        ticker = self.ticker
        data, stockTicker = stockPuller.history(ticker) # Returns pandas dataframe
        X,y,features = stockPuller.dataProcessor(data) # Returns X_train,y_train, and the features to be used
        model = self.trainModel(X,y)
        futurePrice, currentPrice = self.pricePredictor(data, features, model)
        diff = round(futurePrice - currentPrice,2)
        if futurePrice - currentPrice > 0:
            print(f"The predicted closing price of {stockTicker} is {round(futurePrice,3)}$, which is a {diff}$ increase over yesterday!")
        else:
            print(f"The predicted closing price of {stockTicker} is {round(futurePrice,3)}$, which is a {diff}$ decrease over yesterday!")
