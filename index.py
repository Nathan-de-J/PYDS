import yfinance as yf
dat = yf.Ticker("MSFT")

dat = yf.Ticker("MSFT")
print(dat.info)
print(dat.calendar)
dat.analyst_price_targets
dat.quarterly_income_stmt
print(dat.history(period='1mo'))
dat.option_chain(dat.options[0]).calls