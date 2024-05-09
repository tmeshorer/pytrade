from pydantic import BaseModel, ConfigDict


class CompanyDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    sector: str
    subsector: str
    market_cap: float



class CompanyCreate(CompanyDTO):
    pass

class CompanyUpdate(CompanyDTO):
    pass
