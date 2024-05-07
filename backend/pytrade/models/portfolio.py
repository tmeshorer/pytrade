from sqlalchemy import Integer, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column

from pytrade.models.base import Base


class Portfolio(Base):
    __tablename__ = "portfolios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    account_id: Mapped[int] =  mapped_column(Integer, ForeignKey('accounts.id'), index=True)
    cash: Mapped[float] = mapped_column(Float(), nullable=False)
    equity: Mapped[float] = mapped_column(Float(), nullable=False)
    profit: Mapped[float] = mapped_column(Float(), nullable=False)
