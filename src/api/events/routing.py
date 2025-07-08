from fastapi import APIRouter
from .schemas import EventSchema, EventListSchema, EventCreateSchema, EventUpdateSchema

router = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    return {
        "results": [{"id": 1}, {"id": 2}, {"id": 3}],
        "count": 3
    } # type: ignore
    
@router.post("/")
def create_event(payload: EventCreateSchema) -> EventSchema:
    data = payload.model_dump()
    return {
        "id": 123, 
        **data
    } # type: ignore
    

@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {"id": event_id} # type: ignore


@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventSchema:
    data = payload.model_dump()
    return {"id": event_id, **data} # type: ignore