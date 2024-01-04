import matplotlib.pyplot as plt
from app.stock_market.stock_market_model import EquityGeneralData
from decimal import Decimal
import yfinance as yf

# Assuming 'data' is your JSON object and 'Time Series (5min)' is a key in it

class StockMarketData:
    def __init__(self, ticker_symbol):
        self.ticker_symbol = ticker_symbol

    def get_equity_general_data(self) -> EquityGeneralData:
        ticker = yf.Ticker(self.ticker_symbol)
        hist = ticker.history(period="1d", interval="5m")

        latest_data = hist.iloc[-1]
        equity_general_data = EquityGeneralData(
            symbol=self.ticker_symbol,
            open_value=round(Decimal(latest_data['Open']), 2),
            higher_value=round(Decimal(latest_data['High']), 2),
            lower_value=round(Decimal(latest_data['Low']), 2),
            closed_value=round(Decimal(latest_data['Close']), 2),
            volume=latest_data['Volume']
        )
        return equity_general_data
    
    def get_equity_graph(self, time_frame):
        ticker = yf.Ticker(self.ticker_symbol)

        if time_frame == 'diário':
            hist = ticker.history(period="1d", interval="5m")
        elif time_frame == 'semanal':
            hist = ticker.history(period="5d", interval="60m")

        plt.figure(figsize=(30, 15))
        plt.plot(hist['Close'], label='Preço de fechamento')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.title(f'Valor de mercado: {self.ticker_symbol}  - {time_frame.title()}')
        plt.legend()

        return plt
            
    # def get_equity_graph(self):
    #     equity_json_data = self.get_equity_json_data()
    #     equity_graph = None

    #     print(equity_json_data)

    #     if 'Time Series (5min)' in equity_json_data:
    #         df = pd.DataFrame.from_dict(equity_json_data, orient='index')
    #         df = df.rename(columns={'4. close': 'Close'})
    #         df['Close'] = df['Close'].astype(float)
    #         df.index = pd.to_datetime(df.index)

    #         plt.figure(figsize=(10, 4))
    #         plt.plot(df['Close'], label='Close Price')
    #         plt.xlabel('Time')
    #         plt.ylabel('Price')
    #         plt.title('IBM Stock Price')
    #         plt.legend()

    #         equity_graph = plt

    #     return equity_graph
    

            


# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=YOUR_API_KEY'
# r = requests.get(url)
# data = r.json()

# time_series = data['Time Series (5min)']

# # Convert time series data to a Pandas DataFrame
# df = pd.DataFrame.from_dict(time_series, orient='index')
# df = df.rename(columns={'4. close': 'Close'})
# df['Close'] = df['Close'].astype(float)
# df.index = pd.to_datetime(df.index)

# # Plotting
# plt.figure(figsize=(10, 4))
# plt.plot(df['Close'], label='Close Price')
# plt.xlabel('Time')
# plt.ylabel('Price')
# plt.title('IBM Stock Price')
# plt.legend()

# # Display the plot in Streamlit
# st.pyplot(plt)

# if symbol:
#     url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=YOUR_API_KEY'
#     r = requests.get(url)
#     data = r.json()

#     print(data)

#     if 'Meta Data' in data:
#         meta_data = data['Meta Data']
#         st.write(f"**Information:** {meta_data.get('1. Information')}")
#         st.write(f"**Symbol:** {meta_data.get('2. Symbol')}")
#         st.write(f"**Last Refreshed:** {meta_data.get('3. Last Refreshed')}")
#         st.write(f"**Interval:** {meta_data.get('4. Interval')}")
#         st.write(f"**Output Size:** {meta_data.get('5. Output Size')}")
#         st.write(f"**Time Zone:** {meta_data.get('6. Time Zone')}")

#         # Optionally, display the latest data point
#         time_series = data.get('Time Series (5min)', {})
#         latest_time = sorted(time_series.keys())[0]  # Get the latest time
#         latest_data = time_series[latest_time]
#         st.write(f"**Latest Data at {latest_time}**")
#         st.write(f"Open: {latest_data.get('1. open')}")
#         st.write(f"High: {latest_data.get('2. high')}")
#         st.write(f"Low: {latest_data.get('3. low')}")
#         st.write(f"Close: {latest_data.get('4. close')}")
#         st.write(f"Volume: {latest_data.get('5. volume')}")
#     else:
#         st.write("No data available for this symbol or check your API key.")