from pydantic import ConfigDict
from sqlalchemy import Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from pytrade.models.base import Base


class TradeSignalDTO(Base):
    model_config = ConfigDict(from_attributes=True)

    id: int
    portfolio_id: int
    instrument_id : int
    entry_signal_bar_id: int
    entry_action_bar_id: int
    entry_order_id: int
    exit_signal_bar_id: int
    exit_action_bar_id: int
    exit_order_id: int
    position_id: int
    bars: int
    qty: float
    entry_price: float
    exit_price: float

class TradeSignalCreate(TradeSignalDTO):
    pass

class TradeSignalUpdate(TradeSignalDTO):
    pass



