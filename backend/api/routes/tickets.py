from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Ticket(BaseModel):
    title: str
    description: str

@router.get("/")
def get_tickets():
    return [{"id": 1, "title": "Email Issue", "status": "Open"}]

@router.post("/")
def create_ticket(ticket: Ticket):
    return {"message": "Ticket received", "ticket": ticket}
