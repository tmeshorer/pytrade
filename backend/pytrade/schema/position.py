from pydantic import BaseModel, ConfigDict

from pytrade.models.position import PositionDirection


class Position(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    portfolio_id: int
    instrument_id: int
    long_short : PositionDirection
    qty: float
    root: str
    underlying: str
    cost: float
    market_value: float
