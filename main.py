from stockPredictor import stockPredictor


print("NOTE: THE ALPHAVANTAGE API IS LIMITED TO 5 CALLS PER MINUTE AND 100 CALLS PER DAY, IF YOU SEE A REPEATED ERROR EVEN WITH THE CORRECT STOCK TICKER THEN YOU MOST LIKELY HIT THE API LIMIT")
usrTicker = (input("Please enter the stock ticker you wish to use, or type 1 to exit: ")).upper()
while usrTicker != "1":
    stockPredictor(usrTicker)
    usrTicker = (input("Please enter the stock ticker you wish to use, or type 1 to exit: ")).upper()
