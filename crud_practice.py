from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=[]

class Student(BaseModel):
    name:str
    roll_no:int
    
@app.post('/student')
def createstudent(student: Student):
    data.append(student.dict())
    return data
@app.get('/{id}')
def getstudent(id:int):
    return data[id]

@app.put('/data{id}')
def editstudent(id:int,student:Student):
    data[id]=student
    return student
@app.delete('/items/{id}')
def deletedata(id:int):
    data.pop(id)
    return data