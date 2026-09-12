from schemas import TaskCreate
from services import tasks as task_service

def setup_function():
    task_service._tasks.clear()
    task_service._next_id = 1

def test_create_task():
    task = task_service.create_task(TaskCreate(title="buy milk", description="2%"))
    assert task.id == 1
    assert task.title == "buy milk"
    assert task.done is False

def test_get_task_not_found():
    assert task_service.get_task(999) is None

def test_delete_task():
    task = task_service.create_task(TaskCreate(title="test"))
    assert task_service.delete_task(task.id) is True
    assert task_service.get_task(task.id) is None