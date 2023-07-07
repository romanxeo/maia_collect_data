from datetime import datetime
from typing import List

from database import get_db
from models import CollectDataModel
from schemas import CollectDataInput, IdRow, CollectDataOutput
from sqlalchemy import insert, select


async def save_data(data: CollectDataInput) -> IdRow:
    db = get_db()

    input_dict = {
        "input": data.input,
        "output": data.output,
        "symbol": data.symbol,
        "price": data.price,
        "time": datetime.strptime(data.time, '%d.%m.%Y, %H:%M:%S') if data.time else None,
        "first_signal": data.first_signal,
    }

    query_data = insert(CollectDataModel).values(input_dict).returning(CollectDataModel.id)
    output_data = await db.fetch_one(query=query_data)
    id_data = IdRow.parse_obj(output_data)
    return id_data


async def retrieve_data(limit: int, offset: int) -> List[CollectDataOutput]:
    db = get_db()

    query = select([CollectDataModel])
    if limit < 1:
        query = query.limit(1000)
    if offset < 1:
        query = query.offset(0)
    data = await db.fetch_all(query=query)
    return [CollectDataOutput.parse_obj(item) for item in data]


async def save_mass_data(data_list: List[dict]):
    db = get_db()

    input_dict = [{
        "input": data.get("input"),
        "output": data.get("output"),
        "symbol": data.get("symbol"),
        "price": data.get("priceLastUSDT"),
        "time": datetime.strptime(data.get("time"), '%d.%m.%Y, %H:%M:%S') if data.get("time") else None,
        "first_signal": data.get("first_signal"),
    } for data in data_list]

    query_data = insert(CollectDataModel).values(input_dict).returning(CollectDataModel.id)
    await db.fetch_all(query=query_data)
