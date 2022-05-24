import pandas as pd
import yfinance as yf


valuation_cols = ['symbol', 'marketCap','enterpriseValue','currentPrice', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow','earningsGrowth','enterpriseToRevenue', 'enterpriseToEbitda',
                  'forwardEps','trailingEps',  'priceToSalesTrailing12Months', 
                  'forwardPE', 'dividendYield']

def ticker_convert(tick):
    ticker = yf.Ticker(tick)
    ticker_df = pd.DataFrame([ticker.info])
    ticker_df.to_csv(f'{tick}.csv')
    df_ticker = pd.read_csv(f'{tick}.csv')
    ticker_val = df_ticker[valuation_cols]
    return ticker_val