"""FastAPI composition root; ICS door only, no business decisions."""
from fastapi import FastAPI
from app.features.chat.router import router

app = FastAPI(title="Conversational AI Assistant - STEP 1")
app.include_router(router)
