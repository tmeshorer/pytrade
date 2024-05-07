from sqlalchemy import Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from pytrade.models.base import Base


class TradeSignal(Base):
    __tablename__ = "trade_signals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    portfolio_id: Mapped[int] = mapped_column(Integer, ForeignKey('portfolios.id'), index=True)
    instrument_id : Mapped[int] =mapped_column(Integer, ForeignKey('instruments.id'), )
    entry_signal_bar_id: Mapped[int] = mapped_column(Integer, ForeignKey('bars.id'), )
    entry_action_bar_id: Mapped[int] = mapped_column(Integer, ForeignKey('bars.id'), )
    entry_order_id: Mapped[int] = mapped_column(Integer, ForeignKey('orders.id'), )
    exit_signal_bar_id: Mapped[int] = mapped_column(Integer, ForeignKey('bars.id'), )
    exit_action_bar_id: Mapped[int] = mapped_column(Integer, ForeignKey('bars.id'), )
    exit_order_id: Mapped[int] =  mapped_column(Integer, ForeignKey('orders.id'), )
    position_id: Mapped[int] =mapped_column(Integer, ForeignKey('positions.id'), )
    bars: Mapped[int] = mapped_column(Integer, nullable=True)
    qty: Mapped[float] = mapped_column(Float(), nullable=True)
    entry_price: Mapped[float] = mapped_column(Float(), nullable=True)
    exit_price: Mapped[float] = mapped_column(Float(), nullable=True)

