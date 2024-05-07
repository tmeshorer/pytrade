from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from pytrade.models.base import Base


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    sector: Mapped[str] = mapped_column(String(25), nullable=True)
    subsector: Mapped[str] = mapped_column(String(25), nullable=True)
    market_cap: Mapped[float] = mapped_column(Float(), nullable=True)

