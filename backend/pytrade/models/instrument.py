import enum

from sqlalchemy import Integer, ForeignKey, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from pytrade.models.base import Base

class AssetType(enum.Enum):
    STOCK = "stock"
    OPTION = "option"
    FOREX = "forex"
    FUTURE = "future"
    ETF = "etf"


class Instrument(Base):
    __tablename__ = "instruments"

    symbol: Mapped[str] = mapped_column(String(25), primary_key=True,autoincrement=True, index=True)
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey('companies.id'), index=True)
    asset_type: Mapped[AssetType]
    currency: Mapped[str] = mapped_column(String(25), nullable=False)
    exchange: Mapped[str] = mapped_column(String(25), nullable=False, index=True)
    root: Mapped[str] =  mapped_column(String(25), nullable=False)
    underlying: Mapped[str] = mapped_column(String(25), nullable=False, index=True)
    avg_daily_volume: Mapped[float] = mapped_column(Float(), nullable=True)
    one_year_return: Mapped[float] = mapped_column(Float(), nullable=True)
    one_month_return: Mapped[float] = mapped_column(Float(), nullable=True)
    one_week_return: Mapped[float] = mapped_column(Float(), nullable=True)
    one_day_return: Mapped[float] = mapped_column(Float(), nullable=True)
    metric_52_high: Mapped[float] = mapped_column(Float(), nullable=True)
    metric_52_low: Mapped[float] = mapped_column(Float(), nullable=True)

