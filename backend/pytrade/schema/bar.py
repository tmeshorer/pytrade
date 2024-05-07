from datetime import datetime

from pydantic import ConfigDict
from pydantic import BaseModel, ConfigDict

class Bar(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    instrument_id: int
    timestamp: datetime
    high: float
    low: float
    open: float
    close: float
    volume: float
    downTicks: float
    downVolume: float
    totalTicks: float
    upTicks: float
    upVolume: float
    epoch: float
    barStatus: float
    symbol : str
