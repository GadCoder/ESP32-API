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


def get_all_metrics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Metric).offset(skip).limit(limit).all()


def delete_all_metrics(db: Session):
    try:
        db.execute("DELETE FROM ESP32Metrics;")
        db.commit()
        return {"message": "All rows deleted successfully"}
    except Exception as e:
        db.rollback()
        return {"message": f"An error occurred: {str(e)}"}
    finally:
        db.close()
