from sqlalchemy import text
from sqlalchemy.orm import Session
from db.models.metric import Metric
from db.schemas.metric import MetricCreate


def get_metric(db: Session, metric_id: int):
    return db.query(Metric).filter(Metric.id == metric_id).first()


def create_new_metric(db: Session, metric: MetricCreate):
    db_item = Metric(**metric.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_all_metrics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Metric).offset(skip).limit(limit).all()


def delete_all_metrics(db: Session):
    try:
        db.execute(text("DELETE FROM ESP32Metrics;"))
        db.commit()
        return {"message": "All rows deleted successfully"}
    except Exception as e:
        db.rollback()
        return {"message": f"An error occurred: {str(e)}"}
    finally:
        db.close()
