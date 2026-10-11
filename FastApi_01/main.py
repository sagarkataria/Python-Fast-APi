from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")

def read_root():
    return {"message": "welcome to swiggy Order service","status":"Healthy"}



if __name__ == "_name_":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)