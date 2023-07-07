import datetime
from typing import List, Optional

from pydantic.main import BaseModel


class CheckStatus(BaseModel):
    status_code: int
    detail: str
    result: str


class CollectDataInput(BaseModel):
    input: List[float]
    output: List[float]
    symbol: Optional[str]
    price: Optional[float]
    time: Optional[str]
    first_signal: Optional[str]


class IdRow(BaseModel):
    id: int


class CollectDataOutput(CollectDataInput, IdRow):
    time: Optional[datetime.datetime]
    pass



