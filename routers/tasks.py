from fastapi import APIRouter
from services import tasks as task_service
from schemas import TaskCreate, TaskOut

router = APIRouter(prefix='/tasks', tags=['tasks'])

@router.post("/", response_model=TaskOut)
def create_task(task: TaskCreate):
    return task_service.create_task(task)

@router.get("/", response_model=list[TaskOut])
def list_tasks():
    return task_service.list_tasks()

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
    return task_service.get_task(task_id)

@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task: TaskCreate):
    return task_service.update_task(task_id, task)

@router.delete("/{task_id}")
def delete_task(task_id: int):
    return task_service.delete_task(task_id)