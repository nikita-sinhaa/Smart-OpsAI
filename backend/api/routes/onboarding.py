from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Employee(BaseModel):
    name: str
    email: str
    role: str

@router.post("/")
def onboard_employee(emp: Employee):
    return {"message": f"Onboarding initiated for {emp.name}", "details": emp}
