from fastapi import FastAPI,Path
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello, World! Hehe" }

@app.get("/about")

def about():
    l = []
    for i in range(10):
        l.append(i)
    return l

class Item(BaseModel):
    name : str
    price : float
    

inventory = {
    1:{
        "Name":"Milk",
        "Price":4.99
    },
    2:{
        "Name":"Biscuit",
        "Price":6.99
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id:int = Path(...,description="Hello")):
    return inventory[item_id]


#Query Parameters (Question Mark) --- http://127.0.0.1:8000/get-by-name?name=Milk
@app.get("/get-by-name")
def get_item(name:str):
    for i in inventory:
        if inventory[i]["Name"] == name:
            return inventory[i]


#POST AND GET
@app.post("/create-item/{item_id}")
def create_item(item_id:int , item:Item):
    if item_id in inventory:
        return {"Error":"Item already exists"}
    inventory[item_id] = {"Name":item.name,"Price":item.price}
    return inventory[item_id]