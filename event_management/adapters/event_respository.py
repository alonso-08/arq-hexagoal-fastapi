from sqlalchemy.orm import Session
from domain.event import Event

class EventRepository:
    def __init__(self,session: Session) -> None:
        self.session=session

    def persist(self,event: Event):
        self.session.add(event)
        self.session.commit()
    
    def find_by_id(self,id: int):
        return self.session.query(Event).filter(Event.id==id).first()
