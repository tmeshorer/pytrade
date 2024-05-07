from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from pytrade.models.base import Base


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    provider_account_id: Mapped[str] = mapped_column(String(255), nullable=False)
    broker: Mapped[str] = mapped_column(String(25), nullable=False)
    currency: Mapped[str] =  mapped_column(String(25), nullable=False)
    account_type: Mapped[str] = mapped_column()
