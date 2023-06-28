from sqlalchemy.orm import Session

from . import models, schemas


def get_metric(db: Session, metric_id: int):
    return db.query(models.Metric).filter(models.Metric.id == metric_id).first()


def create_metric(db: Session, metric: schemas.MetricCreate):
    db_item = models.Metric(**metric.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
