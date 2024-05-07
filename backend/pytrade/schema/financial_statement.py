from pydantic import BaseModel, ConfigDict
from pytrade.models.base import Base



class FinanicalStatement(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    st_type: str
    qtr: int
    year: int

class FinanicalStatementLineItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    fs_id: int
    name: str
    amount: float


