from fastapi import FastAPI
from fastapi import Request
import uvicorn

app = FastAPI(
    title="Swiggy Order service",
    description=(
        "Internal api for managing orders"
        "Handle creation , tracking of delivery systems"
    ),
    version="1.2.1",
    docs_url="/docs",
    redoc_url="/redocs",
    openapi_url="/openapi.json"

)

@app.get("/")
def read_root():
    """Root endpoint - Health check"""

    # fastapi convert this dict into json

    return {
        "message":"Welcome to swiggy Order service",
        "status":"Healthy"
    }

@app.get("/about")
def about():
    """return api metadata"""
    return {
        "service":"order service",
        "team":"Backend plateform",
        "region":"ap-south-1",
        "version":"1.2.2"
    }