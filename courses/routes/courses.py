from fastapi import APIRouter
from models.courses import courses
from db import get_database

router = APIRouter()

@router.post("/courses", tags=["courses"])
async def insert_courses(id, title, course_description, duration, language, course_classroom, created_date, updated_date):
    insert_stmt = courses.insert().values(id=id, title=title, course_description=course_description, duration=duration, language=language, course_classroom=course_classroom, created_date=created_date, updated_date=updated_date)
    database = get_database()
    await database.execute(insert_stmt)
    return {
        "id": id,
        "title": title,
        "course_description": course_description,
        "duration": duration,
        "language": language,
        "course_classroom": course_classroom,
        "created_date": created_date,
        "updated_date": updated_date
        }

@router.get("/courses-data")
async def retrieve_courses():
    select_stmt = courses.select()
    result = await get_database().fetch_all(select_stmt)
    return result

@router.get("/courses/{id}")
async def retrieve_individual_courses(
    id: int

):
    select_stmt = courses.select().where(courses.c.id == id)
    result = await get_database().fetch_one(select_stmt)
    return result



