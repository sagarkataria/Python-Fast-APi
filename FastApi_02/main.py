from fastapi import FastAPI, Query , HTTPException
from models import MenuResponse,MenuItem
from data import data


app = FastAPI(
    title = "Point menu",
    description = "Read only menu API for Kiosk display and mobile app"
)

@app.get("/")

def root():
    return {"message":"Welcome to fatsapi"}


@app.get("/menu" ,response_model = MenuResponse)
def get_menu(category:str | None =  Query(None,description = "Filter by chai, snack or combo")):
    if category:
        filtered = [item for item in data if item["category"] == category.lower()]
        if not filtered:
            raise HTTPException(status_code = 404,detail=f"No found in details category:{category}")
        return MenuResponse(count=len(filtered),items=filtered)
    return MenuResponse(count = len(data),items=data)


@app.get("/menu/{item_id}",response_model=MenuItem)
def get_item(item_id:int):
    # print('data',data)
    print('item_id',item_id)
    for item in data:
        if item['id'] == item_id:
            return item
    raise HTTPException(status_code = 404,detail=f"No found in details category:{item_id}")
