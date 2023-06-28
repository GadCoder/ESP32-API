from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from db import crud, models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/metrics/create-metric", response_model=schemas.Metric)
def create_metric(metric: schemas.MetricCreate, db: Session = Depends(get_db)):
    return crud.create_metric(db=db, metric=metric)


@app.get("/metrics/read-metric/{metric_id}", response_model=schemas.Metric)
def read_metric(metric_id: int, db: Session = Depends(get_db)):
    db_metric = crud.get_metric(db=db, metric_id=metric_id)
    if db_metric is None:
        raise HTTPException(status_code=404, detail="Metric not found")
    return db_metric


@app.get("/metrics/get-all-metrics/", response_model=list[schemas.Metric])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrics = crud.get_all_metrics(db, skip=skip, limit=limit)
    return metrics


@app.delete("/metrics/delete-all-metrics/")
def delete_all_metrics(db: Session = Depends(get_db)):
    return crud.delete_all_metrics(db=db)
