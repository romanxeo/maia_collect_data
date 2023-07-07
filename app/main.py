import uvicorn
from database import get_db, prepare_db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router
from settings import settings
from logger import Logger

description = """
## Collect data for Maia
"""

app = FastAPI(
    title='Collect data for Maia',
    description=description,
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True,
)

app.include_router(router, tags=["Common"])


@app.on_event('startup')
async def startup():
    await get_db().connect()
    await prepare_db()
    Logger.info('startup')


@app.on_event('shutdown')
async def shutdown():
    await get_db().disconnect()
    Logger.info('shutdown')


def main():
    uvicorn.run(
        'main:app',
        reload=True,
        host=settings.APP_HOST,
        port=settings.APP_PORT
    )


if __name__ == '__main__':
    main()
