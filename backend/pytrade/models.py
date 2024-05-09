import enum
from datetime import datetime
from typing import Optional
from uuid import uuid4

from sqlalchemy import Integer, String, DateTime, func, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from . import db, Base


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    broker_account_id: Mapped[str] = mapped_column(String(255), nullable=True)
    broker: Mapped[str] = mapped_column(String(25), nullable=True)
    currency: Mapped[str] =  mapped_column(String(25), nullable=True,default="USD")
    account_type: Mapped[str] = mapped_column()

    @staticmethod
    def find(id) :
        return db.session.execute(db.select(Account).where(Account.id == id))

    @staticmethod
    def seed_data_if_empty():
        if len(db.session.execute(db.select(Account)).scalars().all()) > 0:
            return False
        # if there are no quizzes, create a quiz and add questions
        account: Account = Account(broker="Swab",currency="USD")
        db.session.add(account)
        db.session.commit()


        questions = [
            Question(
                question="Who invented Python?",
                answer="Guido van Rossum",
                choices=["Guido van Rossum", "Ada Lovelace", "Rob Pike", "Kathleen Booth"],
                quiz_id=quiz.id,
            ),
            Question(
                question="What is the name of the Python package installer?",
                answer="pip",
                choices=["pip", "py", "package", "install"],
                quiz_id=quiz.id,
            ),
            Question(
                question="What was Python named after?",
                answer="Monty Python, the comedy group",
                choices=[
                    "Python, the type of snake",
                    "Monty Python, the comedy group",
                    "Python of Aenus, the philosopher",
                    "Ford Python, a race car",
                ],
                quiz_id=quiz.id,
            ),
            Question(
                question="When was the first version of Python released?",
                answer="1991",
                choices=["1971", "1981", "1991", "2001", "2011"],
                quiz_id=quiz.id,
            ),
        ]
        db.session.add_all(questions)
        db.session.commit()
        return True

class Bar(Base):
    __tablename__ = "bars"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    instrument_id: Mapped[int] = mapped_column(Integer, ForeignKey('instruments.id'), index=True)
    timestamp: Mapped[Optional[datetime]] = mapped_column(nullable=True)
    daily_index: Mapped[int] =  mapped_column(Float(), nullable=False)
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
    symbol : Mapped[str] = mapped_column(String(25), nullable=True)


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    sector: Mapped[str] = mapped_column(String(25), nullable=True)
    subsector: Mapped[str] = mapped_column(String(25), nullable=True)
    market_cap: Mapped[float] = mapped_column(Float(), nullable=True)



class FSType(enum.Enum):
    BALANCE_SHEET = "balancesheet"
    INCOME = "income"
    CASHFLOW = "cashflow"

class FinanicalStatement(Base):
    __tablename__ = "financial_statements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey('companies.id'), index=True)
    st_type: Mapped[FSType]
    qtr: Mapped[int] = mapped_column(Integer, ForeignKey('companies.id'), index=True)
    year: Mapped[int] = mapped_column(Integer, ForeignKey('companies.id'), index=True)

class FinanicalStatementLineItem(Base):
    __tablename__ = "financial_statement_line_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    fs_id: Mapped[int] = mapped_column(Integer, ForeignKey('financial_statements.id'), index=True)
    name: Mapped[str] = mapped_column()
    amount: Mapped[float] = mapped_column(Float(), nullable=False)


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


class Portfolio(Base):
    __tablename__ = "portfolios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    account_id: Mapped[int] =  mapped_column(Integer, ForeignKey('accounts.id'), index=True)
    cash: Mapped[float] = mapped_column(Float(), nullable=False)
    equity: Mapped[float] = mapped_column(Float(), nullable=False)
    profit: Mapped[float] = mapped_column(Float(), nullable=False)


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

