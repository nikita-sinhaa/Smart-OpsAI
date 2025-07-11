from fastapi import FastAPI
from backend.api.routes import tickets, onboarding

app = FastAPI(title="SmartOps.AI API")

app.include_router(tickets.router, prefix="/tickets", tags=["Ticket Management"])
app.include_router(onboarding.router, prefix="/onboarding", tags=["Onboarding"])
