from models.event import Event


class EventService:
    def __init__(self, event_repository) -> None:
        self.event_repository=event_repository

    def create_event(self, start_date: str, end_date: str):
        event=Event(self.event_repository.next_id(), start_date=start_date, end_date=end_date)
        self.event_repository.persist(event)
        return event

    def get_event(self, id: int):
        return self.event_repository.find_by_id(id)
    
    def cancel_event(self, id: int):
        event=self.event_repository.find_by_id(id)
        if event is None:
            raise Exception("Event not found")
        event.cancelled=True
        self.event_repository.persist(event)
