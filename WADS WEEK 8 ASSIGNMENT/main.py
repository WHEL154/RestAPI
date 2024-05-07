from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    id: int
    title: str
    status: bool

task = [
    Task(id=1, title="Task 1", status=False),
    Task(id=2, title="Task 2", status=True)
]

@app.get("/tasks/", response_model=List[Task]) # provide a list of stored tasks
async def get_tasks():
    return task

@app.get("/tasks/{task_id}", response_model=Task) # get the task by ID
async def get_task(task_id: int):
    for task in task:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks/", response_model=Task, status_code=201) # create a new tassk
async def create_task(task: Task):
    if task.id in [t.id for t in task]:  # Check if task ID already exists
        raise HTTPException(status_code=400, detail="Task ID already exists")
    task.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task) # update the task by ID
async def update_task(task_id: int, task_data: Task):
    for t in task:
        if t.id == task_id:
            t.title = task_data.title
            t.status = task_data.status
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=204) # delete the task by ID
async def delete_task(task_id: int):
    for i, task in enumerate(task):
        if task.id == task_id:
            del task[i]
            return
    raise HTTPException(status_code=404, detail="Task not found")
