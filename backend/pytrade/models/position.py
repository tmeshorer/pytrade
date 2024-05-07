import enum

from sqlalchemy import Integer, ForeignKey, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from pytrade.models.base import Base

class PositionDirection(enum.Enum):
   LONG = "long"
   SHORT = "short"
class Position(Base):
    __tablename__ = "positions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    portfolio_id: Mapped[int] = mapped_column(Integer, ForeignKey('portfolios.id'), index=True)
    instrument_id: Mapped[int] = mapped_column(Integer, ForeignKey('instruments.id'))
    long_short : Mapped[PositionDirection]
    qty: Mapped[float] = mapped_column(Float(), nullable=False)
    root: Mapped[str] = mapped_column(String(255), nullable=True)
    underlying: Mapped[str] = mapped_column(String(255), nullable=True)
    cost: Mapped[float] =mapped_column(Float(), nullable=True)
    market_value: Mapped[float] = mapped_column(Float(), nullable=True)
