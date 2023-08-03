from stockPredictor import stockPredictor
from stockPuller import stockPuller

def main(usrTicker):
    apiKey= "Enter API Key here"
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={usrTicker}&outputsize=full&apikey={apiKey}&datatype=csv'

    checker = stockPuller.stockChecker(url = url)
    while not checker:
        usrTicker = (input("Sorry, the ticker you have inputted seems to be incorrect, please type a new one in: ")).upper()
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={usrTicker}&outputsize=full&apikey={apiKey}&datatype=csv'
        checker = stockPuller.stockChecker(url = url)


    stockPredictor(usrTicker)

print("NOTE: THE ALPHAVANTAGE API IS LIMITED TO 5 CALLS PER MINUTE AND 100 CALLS PER DAY, IF YOU SEE A REPEATED ERROR EVEN WITH THE CORRECT STOCK TICKER THEN YOU MOST LIKELY HIT THE API LIMIT")
usrTicker = (input("Please enter the stock ticker you wish to use, or type 1 to exit: ")).upper()
while usrTicker != "1":
    main(usrTicker)
    usrTicker = (input("Please enter the stock ticker you wish to use, or type 1 to exit: ")).upper()
