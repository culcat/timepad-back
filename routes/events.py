from typing import List

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db import getdb
from services import events as event_service
from dto.events import Event

router = APIRouter()

@router.get("/events", tags=['events'])
async def get_events(db: Session = Depends(getdb)):
    return event_service.get_events(db)

@router.get("/events/{id}", tags=['events'])
async def get_event(id: int, db: Session =Depends(getdb)):
    return event_service.get_event(id,db)

@router.post("/events", tags=['events'])
async def create_event(data: Event, db: Session = Depends(getdb)):
    return event_service.create_event(data,db)

@router.delete("/events/{id}", tags=['events'])
async def delete_event(id: int, db: Session = Depends(getdb)):
    return event_service.delete_event(id,db)