
from fastapi import FastAPI
from . import  models
from. import schemas
from . database import engine






from typing import Optional
from pydantic import BaseModel
app=FastAPI()
models.Base.metadata.create_all(engine)
@app.get('/')
def ab():
    return {'data':{'name':'ABDULLAH'}}
@app.get('/about')
def a():
    return {'data': 'about page'}
# path parameters
@app.get('/items/{id}')
def index(id:int):
    return {"product id ": id}
# query parameters
@app.get('/items/')
def index(q:int=0,m:Optional[int]=10):
    return {"item is ": q,"m":m}

@app.get('/items/{file_path:path}')
def index(file_path:str):
    return {"file_path":file_path}

# request body
class blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]



@app.post('/items/')
def index(blog:blog):
   
    return {'data': f"blog is created with title {blog.title} and {blog.body}"}