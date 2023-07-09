from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException
from db.session import get_db
from db.schemas.pill import PillCreate, Pill
from db.repository.pill import get_is_pill_time, create_new_pill, get_pill, get_all_pills, delete_all_pills

router = APIRouter()


@router.get("/pills/is_pill_time/")
def is_pill_time(db: Session = Depends(get_db)):
    pill_asigned = get_is_pill_time(db=db)
    if pill_asigned is None:
        raise HTTPException(
            status_code=404, detail="There's not pill asignned to this time and day")
    return pill_asigned


@router.post("/pills/create-pill", response_model=Pill)
def create_pill(pill: PillCreate, db: Session = Depends(get_db)):
    return create_new_pill(db=db, pill=pill)


@router.get("/pills/read-pill/{pill_id}", response_model=Pill)
def read_pill(pill_id: int, db: Session = Depends(get_db)):
    db_pill = get_pill(db=db, pill_id=pill_id)
    if db_pill is None:
        raise HTTPException(status_code=404, detail="pill not found")
    return db_pill


@router.get("/pills/get-all-pills/", response_model=list[Pill])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pills = get_all_pills(db, skip=skip, limit=limit)
    return pills


@router.delete("/pills/delete-all-pills/")
def delete_pills(db: Session = Depends(get_db)):
    return delete_all_pills(db=db)
