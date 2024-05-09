from pydantic import BaseModel, ConfigDict
from pytrade.models.base import Base



class FinanicalStatementDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    st_type: str
    qtr: int
    year: int

class FinanicalStatementLineItemDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    fs_id: int
    name: str
    amount: float


