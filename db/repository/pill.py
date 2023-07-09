from sqlalchemy import text
from sqlalchemy.orm import Session
from db.models.pill import Pill
from db.schemas.pill import PillCreate
from datetime import datetime
import pytz


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


def get_is_pill_time(db: Session):
    # Specify the desired timezone
    timezone = pytz.timezone('America/Lima')

    # Get the current datetime in the specified timezone
    current_datetime = datetime.now(timezone)

    # Extract the day, hour, and minute components
    current_day = current_datetime.strftime('%A')  # Full weekday name
    current_hour = current_datetime.strftime('%H')  # Hour in 24-hour format
    current_minute = current_datetime.strftime('%M')  # Minute
    current_time = current_hour + ":" + current_minute
    print(current_day)
    print(current_time)
    return db.query(Pill).filter(Pill.day == current_day, Pill.time == current_time).first()
