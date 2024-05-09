from pydantic import BaseModel, ConfigDict


class IndicatorDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class IndicatorCreate(IndicatorDTO):
    pass

class IndicatorUpdate(IndicatorDTO):
    pass
