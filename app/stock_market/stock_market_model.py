from pydantic import BaseModel
from decimal import Decimal

class EquityGeneralData(BaseModel):
    symbol: str
    open_value: Decimal
    higher_value: Decimal
    lower_value: Decimal
    closed_value: Decimal
    volume: int

        # equity_general_data = EquityGeneralData(
        #     symbol=self.ticker_symbol,
        #     open_value=latest_data['Open'],
        #     higher_value=latest_data['High'],
        #     lower_value=latest_data['Low'],
        #     closed_value=latest_data['Close'],
        #     volume=latest_data['Volume']
        # )