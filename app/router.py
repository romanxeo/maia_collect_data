from typing import List

from fastapi import APIRouter, Depends
from schemas import CheckStatus, CollectDataInput, IdRow, CollectDataOutput
from service import save_data, retrieve_data
from utils import validate_request

router = APIRouter()


@router.get("/", response_model=CheckStatus)
async def check_status() -> CheckStatus:
    return CheckStatus(
        status_code=200,
        detail='ok',
        result='working'
    )


@router.get("/get_system_logs/")
async def get_logs(validate=Depends(validate_request)):
    with open(file="logger.info", mode="r") as file:
        response = file.readlines()
    return response


@router.post("/save/", response_model=IdRow)
async def r_save_data(data: CollectDataInput,
                      validate=Depends(validate_request)) -> IdRow:
    return await save_data(data=data)


@router.get("/retrieve/", response_model=List[CollectDataOutput])
async def r_retrieve_data(validate=Depends(validate_request),
                          limit: int = 1000,
                          offset: int = 0,
                          ) -> List[CollectDataOutput]:
    return await retrieve_data(limit=limit, offset=offset)
