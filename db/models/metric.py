from sqlalchemy import Column, Integer, Float, DateTime, String
from db.session import Base


class Metric(Base):
    __tablename__ = "ESP32Metrics"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    record_time = Column(DateTime)
    value = Column(Float)
    type = Column(String)
