from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from pytrade.models.base import Base


class Indicator(Base):
    __tablename__ = "indicators"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    name: Mapped[str] = mapped_column()
