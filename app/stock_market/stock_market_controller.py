import matplotlib.pyplot as plt
from app.stock_market.stock_market_model import EquityGeneralData
from decimal import Decimal
import yfinance as yf


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
            