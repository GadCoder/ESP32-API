from sqlalchemy import text
from sqlalchemy.orm import Session
from db.models.pill import Pill
from db.schemas.pill import PillCreate


def get_pill(db: Session, pill_id: int):
    return db.query(Pill).filter(Pill.id == pill_id).first()


def create_new_pill(db: Session, pill: PillCreate):
    db_item = Pill(**pill.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_all_pills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pill).offset(skip).limit(limit).all()


def delete_all_pills(db: Session):
    try:
        db.execute(text("DELETE FROM pill;"))
        db.commit()
        return {"message": "All rows deleted successfully"}
    except Exception as e:
        db.rollback()
        return {"message": f"An error occurred: {str(e)}"}
    finally:
        db.close()


def get_is_pill_time(day: str, time: str, db: Session):
    return db.query(Pill).filter(Pill.day == day, Pill.time == time).first()
