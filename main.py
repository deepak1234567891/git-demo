from fastapi import FastAPI
from models.contact_form import metadata, contact_form
from db import Database
import sqlalchemy
from db import sqlalchemy_engine
from router.contact_form import router as contact_form_router


app = FastAPI()


DATABASE_URL = "sqlite:///contact_form.db"
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
app.include_router(contact_form_router)