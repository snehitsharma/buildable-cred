from schemas import TaskCreate, TaskOut

_tasks: dict[int, TaskOut] = {}
_next_id = 1

def create_task(task: TaskCreate) -> TaskOut:
    global _next_id
    new_task = TaskOut(id=_next_id, **task.model_dump())
    _tasks[_next_id] = new_task
    _next_id += 1
    return new_task

def list_tasks() -> list[TaskOut]:
    return list(_tasks.values())

def get_task(task_id: int) -> TaskOut | None:
    return _tasks.get(task_id)

def update_task(task_id: int, task: TaskCreate) -> TaskOut | None:
    if task_id not in _tasks:
        return None
    updated = TaskOut(id=task_id, **task.model_dump())
    _tasks[task_id] = updated
    return updated

def delete_task(task_id: int) -> bool:
    return _tasks.pop(task_id, None) is not None