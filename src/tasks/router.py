from fastapi import APIRouter,Depends,status
from src.tasks import controller as task_controller
from src.tasks.dtos import TaskSchema,Taskresponsescchema
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session


task_routes = APIRouter(prefix="/tasks")


@task_routes.post('/create',status_code=status.HTTP_201_CREATED,response_model=Taskresponsescchema)
def create_task(body: TaskSchema,db:Session=Depends(get_db)):
    return task_controller.create_task(body,db)

@task_routes.get("/all_task",response_model=List[Taskresponsescchema],status_code=status.HTTP_200_OK)
def get_all_tasks(db:Session=Depends(get_db)):
    return task_controller.get_task(db)

@task_routes.get("/one_task/{task_id}",response_model=Taskresponsescchema,status_code=status.HTTP_200_OK)
def specific_task(task_id:int,db:Session=Depends(get_db)):
    return task_controller.one_task(task_id,db)

@task_routes.put("/update_task/{task_id}",response_model=Taskresponsescchema,status_code=status.HTTP_201_CREATED)
def update_task(task_id:int,body:TaskSchema,db:Session=Depends(get_db)):
    return task_controller.update_task(task_id,body,db)

@task_routes.delete("/delete_task/{task_id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db:Session=Depends(get_db)):
    return task_controller.delete_task(task_id,db)