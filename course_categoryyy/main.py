from fastapi import FastAPI
from models.course_category import metadata, course_category
from db import Database
import sqlalchemy
from db import sqlalchemy_engine
from router.course_category import router as course_category_router


app = FastAPI()


DATABASE_URL = "sqlite:///course_category.db"
database = Database(DATABASE_URL)
sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)


@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(sqlalchemy_engine)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

metadata.create_all(sqlalchemy_engine)
app.include_router(course_category_router)