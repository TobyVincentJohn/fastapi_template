from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()


class Item(BaseModel):
    name:str
    description:str=None
    price:float
    tax:float=None  

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.post("/items/")
async def create_item(item:Item):
    return item.price+item.tax

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/me")
async def read_user():
    return ["hello" , "world"]

@app.get("/items/")
async def read_item(skip:int=0,limit:int=10):
    return fake_items_db[skip:skip+limit]

@app.get("/items/{item_id}")
async def read_item(item_id:int, q:str=None,short:bool=False):
    item={"item_id":item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description":"This is an amazing item that has a long description"}
        )
    else:
        item.update(
            {"description":"This is an amazing item"}
        )
    return item