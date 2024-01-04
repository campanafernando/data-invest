from pydantic import BaseModel
from decimal import Decimal

class EquityGeneralData(BaseModel):
    symbol: str
    open_value: Decimal
    higher_value: Decimal
    lower_value: Decimal
    closed_value: Decimal
    volume: int
