from fastapi import FastAPI
# import sqlalchemy
from db import get_database,sqlalchemy_engine
from models.courses import courses_metadata
from routes.courses import router as courses_router

# pip install fastapi sqlalchemy pymysql aiomysql databases uvicorn

# DATABASE_URL = "sqlite:///person.db"
# #
# sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)
#

app = FastAPI()

@app.on_event("startup")
async def startup():
  await get_database().connect()


@app.on_event("shutdown")
async def shutdown():
  await get_database().disconnect()

courses_metadata.create_all(sqlalchemy_engine)
app.include_router(courses_router, prefix="")