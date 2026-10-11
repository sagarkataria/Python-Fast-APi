from fastapi import FastAPI


app = FastAPI(
    title = "Point menu",
    description = "Read only menu API for Kiosk display and mobile app"
)

@app.get("/")

def root():
    return {"message":"Welcome to fatsapi"}