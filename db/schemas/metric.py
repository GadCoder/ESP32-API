from pydantic import BaseModel


class MetricBase(BaseModel):
    value: float
    type: str


class MetricCreate(MetricBase):
    pass


class Metric(MetricBase):
    id: int

    class Config:
        orm_mode = True
