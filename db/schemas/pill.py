from pydantic import BaseModel


class PillBase(BaseModel):
    day: str
    time: str
    pill_name: str


class PillCreate(PillBase):
    pass


class Pill(PillBase):
    id: int

    class Config:
        orm_mode = True
