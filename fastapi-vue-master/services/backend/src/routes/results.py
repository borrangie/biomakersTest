from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.results as crud
from src.auth.jwthandler import get_current_user
from src.schemas.results import ResultOutSchema, ResultInSchema, UpdateResult
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/results",
    response_model=List[ResultOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_results():
    return await crud.get_results()


@router.get(
    "/result/{result_id}",
    response_model=ResultOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_result(result_id: int) -> ResultOutSchema:
    try:
        return await crud.get_result(result_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Result does not exist",
        )


@router.post(
    "/results", response_model=ResultOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_result(
    result: ResultInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> ResultOutSchema:
    return await crud.create_result(result, current_user)


@router.patch(
    "/result/{result_id}",
    dependencies=[Depends(get_current_user)],
    response_model=ResultOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_result(
    result_id: int,
    result: UpdateResult,
    current_user: UserOutSchema = Depends(get_current_user),
) -> ResultOutSchema:
    return await crud.update_result(result_id, result, current_user)


@router.delete(
    "/result/{result_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_result(
    result_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_result(result_id, current_user)
