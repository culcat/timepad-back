from fastapi import Depends
from sqlalchemy.orm import Session
from models.events import Events
from dto.events import Event as EventDto

def create_event(data: EventDto ,db: Session):
    event = Events(name=data.name, description=data.description,img=data.img,date=data.date,location=data.location,status=data.status,members=data.members)
    try:
        db.add(event)
        db.commit()
        db.refresh(event)
    except Exception as e:
        print(e)
    return event


def get_events(db: Session):
    return  db.query(Events).all()


def get_event(id: int, db: Session):
    return db.query(Events).filter(Events.id == id).first()

def delete_event(id: int, db: Session):
    event = db.query(Events).filter(Events.id == id).delete()
    db.commit()
    return event