import pandas as pd
class stockPuller:
    def main_puller(ticker):
        while True:
            try:
                training_data, stockTicker = stockPuller.history(ticker)
                training_data['timestamp'] # This checks to see if the dataframe contains a timestamp column, which makes sure the training_data is valid data.
            except KeyError:
                ticker = input("Sorry, the ticker you have inputted might be incorrect, please type a new one: ")
            except Exception as error:
                print("Sorry, an error has occurred:",error)
                exit()
            else:
                return training_data, stockTicker
    def history(ticker):
        apiKey = "Enter your API key here"
        stockTicker = ticker.upper()
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stockTicker}&outputsize=full&apikey={apiKey}&datatype=csv'
        training_data = pd.read_csv(url) # Converts the data into a pandas dataframe
        return training_data, stockTicker
    def dataProcessor(data):
        prevClose = data
        prevClose['timestamp'] = pd.to_datetime(prevClose['timestamp'])
        prevClose['Previous Close'] = prevClose['close'].shift(1)
        prevClose=prevClose.dropna(axis=0)# Drop first row since that contains no previous close value thus having a nan
        # Getting features that will be used for training
        y = prevClose["close"]
        features = ["Previous Close", "high", "low", "open"]
        X = pd.get_dummies(prevClose[features])
        return (X,y,features)
        
