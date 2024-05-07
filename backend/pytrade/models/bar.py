from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from pytrade.models.base import Base


class Bar(Base):
    __tablename__ = "bars"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    instrument_id: Mapped[int] = mapped_column(Integer, ForeignKey('instruments.id'), index=True)
    timestamp: Mapped[Optional[datetime]] = mapped_column(nullable=True)
    high: Mapped[float] =  mapped_column(Float(), nullable=False)
    low: Mapped[float] = mapped_column(Float(), nullable=False)
    open: Mapped[float] = mapped_column(Float(), nullable=False)
    close: Mapped[float] =mapped_column(Float(), nullable=False)
    volume: Mapped[float] = mapped_column(Float(), nullable=False)
    downTicks: Mapped[float] = mapped_column(Float(), nullable=True)
    downVolume: Mapped[float] =  mapped_column(Float(), nullable=True)
    totalTicks: Mapped[float] =  mapped_column(Float(), nullable=True)
    upTicks: Mapped[float] =  mapped_column(Float(), nullable=True)
    upVolume: Mapped[float] = mapped_column(Float(), nullable=True)
    epoch: Mapped[float] = mapped_column()
    barStatus: Mapped[float] = mapped_column()
    symbol : Mapped[str] = mapped_column()
