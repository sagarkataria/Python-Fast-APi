from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
from routes.reviews import router as review_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tables()
    print("Database table created")
    yield
    # Shutdown cleanup here
    print("Shutting down the app")


app = FastAPI(
    title = "Rangmanch Review API",
    description = "Theatre review API for Pune Rangmanch",
    lifespan = lifespan
)

app.include_router(review_router)

@app.get("/")
def root():
    return {
        "message":"Welcome to Rangmanch Api"
    }