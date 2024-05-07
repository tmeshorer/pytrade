import enum

from sqlalchemy import Integer, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from pytrade.models.base import Base

class OrderType(enum.Enum):
    LIMIT = "limit"
    MARKET = "market"
    STOP = "stop"

class TimeInForce(enum.Enum):
    DAY = "day"
    GTC = "gtc"

class QtyUnits(enum.Enum):
   SHARES = "shares"
   USD = "usd"


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    portfolio_id: Mapped[int] = mapped_column(Integer, ForeignKey('portfolios.id'), index=True)
    instrument_id: Mapped[int] = mapped_column(Integer, ForeignKey('instruments.id'), index=True)
    currency: Mapped[str] = mapped_column(String(255), nullable=True)
    symbol: Mapped[str] = mapped_column()
    open_date_time: Mapped[str] = mapped_column()
    order_type: Mapped[OrderType]
    qty: Mapped[float] = mapped_column(Float(), nullable=False)
    price: Mapped[float] = mapped_column(Float(), nullable=False)
    unit:Mapped[QtyUnits]
    time_in_force:Mapped[TimeInForce]
    status: Mapped[str] = mapped_column(String(255), nullable=True)



class OrderLeg(Base):
    __tablename__ = "orderlegs"

    parent_id: Mapped[int] = mapped_column(Integer, ForeignKey('orders.id'), index=True)
    order_type: Mapped[OrderType]
    qty: Mapped[float] = mapped_column(Float(), nullable=False)
    price: Mapped[float] = mapped_column(Float(), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=True)
