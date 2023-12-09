from fastapi import Depends, FastAPI, HTTPException
from domain.event import Event
from adapters.event_respository import EventRepository
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import get_db
from fastapi import APIRouter
from domain.event import EventService

router = APIRouter()

@router.post("/event/")
def create_event(start_date: str, end_date: str, db: Session=Depends(get_db)):
    event=Event(start_date=start_date, end_date=end_date)
    event_repository=EventRepository(db)
    event_repository.persist(event)
    return event

@router.get("/event/{id}")
def get_event(id: int, db: Session = Depends(get_db)):
    event_service = EventService(EventRepository(db))
    event = event_service.get_event(id)
    if event is None:
        return {"error": "Event not found"}, 404
    return {"id": event.id, "start_date": event.start_date, "end_date": event.end_date, "cancelled": event.cancelled}
