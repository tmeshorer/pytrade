import enum

from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from pytrade.models.base import Base



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


