from typing import Annotated
from fastapi.params import Depends

from repository import TaskRepository
from schemas import STask, STaskAdd
from fastapi import APIRouter

router = APIRouter(
    # prefix='/tasks',
    tags=['Tasks']
)

@router.get('/tasks')
async def get_tasks():
    task_list = await TaskRepository.find_all()
    return {'data': task_list}

@router.post('/tasks')
async def post_task(
        task: STaskAdd
        # task: Annotated[STaskAdd, Depends()]
):
     # print(task)

     task_id = await TaskRepository.add_one(task)
     return {'OK': True, 'task_id': task_id}
