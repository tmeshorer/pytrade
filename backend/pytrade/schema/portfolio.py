from sqlalchemy import Integer, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column

from pytrade.models.base import Base
from pydantic import BaseModel, ConfigDict

class Portfolio(Base):
    model_config = ConfigDict(from_attributes=True)


    id: int
    account_id: int
    cash: float
    equity: float
    profit: float
