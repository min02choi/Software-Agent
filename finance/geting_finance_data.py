import yfinance as yf

# 예: Apple 주식 데이터 가져오기 (AAPL)
stock_data = yf.download('AAPL', start='2025-03-21', end='2025-03-26')

# 데이터 출력
print(stock_data.head())
