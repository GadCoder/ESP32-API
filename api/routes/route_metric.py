from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException
from db.session import get_db
from db.schemas.metric import Metric, MetricCreate
from db.repository.metric import create_new_metric, get_metric, get_all_metrics, delete_all_metrics


router = APIRouter()


@router.post("/metrics/create-metric", response_model=Metric)
def create_metric(metric: MetricCreate, db: Session = Depends(get_db)):
    return create_new_metric(db=db, metric=metric)


@router.get("/metrics/read-metric/{metric_id}", response_model=Metric)
def read_metric(metric_id: int, db: Session = Depends(get_db)):
    db_metric = get_metric(db=db, metric_id=metric_id)
    if db_metric is None:
        raise HTTPException(status_code=404, detail="Metric not found")
    return db_metric


@router.get("/metrics/get-all-metrics/", response_model=list[Metric])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrics = get_all_metrics(db, skip=skip, limit=limit)
    return metrics


@router.delete("/metrics/delete-all-metrics/")
def delete_metrics(db: Session = Depends(get_db)):
    return delete_all_metrics(db=db)
