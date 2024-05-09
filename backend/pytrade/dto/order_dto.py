import enum

from sqlalchemy import Integer, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from pytrade.models.base import Base
from pytrade.models.order import QtyUnits, OrderType, TimeInForce
from pydantic import BaseModel, ConfigDict

class OrderDTO(Base):
    model_config = ConfigDict(from_attributes=True)

    id: int
    portfolio_id: int
    instrument_id: int
    currency: str
    symbol: str
    open_date_time: str
    order_type: OrderType
    qty: float
    price: float
    unit: QtyUnits
    time_in_force: TimeInForce
    status: str



class OrderLegDTO(Base):
    model_config = ConfigDict(from_attributes=True)

    parent_id: int
    order_type: OrderType
    qty: float
    price: float
    status: str


class OrderCreate(OrderDTO):
    pass

class OrderUpdate(OrderDTO):
    pass


class OrderLegCreate(OrderLegDTO):
    pass

class OrderLegUpdate(OrderLegDTO):
    pass
