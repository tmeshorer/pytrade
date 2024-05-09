from pydantic import BaseModel, ConfigDict

class InstrumentDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    symbol: str
    company_id: int
    asset_type: str
    currency: str
    exchange: str
    root: str
    underlying: str
    avg_daily_volume: float
    one_year_return: float
    one_month_return: float
    one_week_return: float
    one_day_return: float
    metric_52_high: float
    metric_52_low: float


class InstrumentCreate(InstrumentDTO):
    pass

class InstrumentUpdate(InstrumentDTO):
    pass
