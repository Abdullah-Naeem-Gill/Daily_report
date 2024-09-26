from fastapi import FastAPI
from pydantic import BaseModel  

app=FastAPI()
data=[]

class Book(BaseModel):
    title:str
    author:str
    publisher:str
@app.post('/book')
def createbook(book: Book):
    data.append(book.dict())
    return data

@app.get('/{id}')
def readbook(id:int):
    return data[id]
@app.put('/data{id}')
def editbook(id:int,book:Book):
    data[id]=book
    return book
@app.delete('/item/{id}')
def deletebook(id:int):
    data.pop(id)
    return data
    