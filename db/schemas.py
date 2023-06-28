from pydantic import BaseModel
from datetime import datetime


class MetricBase(BaseModel):
    record_time = datetime
    value: float
    type: str


class MetricCreate(MetricBase):
    pass


class Metric(MetricBase):
    id: int

    class Config:
        orm_mode = True
