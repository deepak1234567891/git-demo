from pydantic import BaseModel,EmailStr
from fastapi import status,APIRouter,HTTPException,Header
from datetime import datetime
from db import get_database
from models.course_content import course_content


router=APIRouter()


class UserBase(BaseModel):
    id: int
    name: str
    duration: str
    course_id: int
    created_date: datetime
    updated_date: datetime

# class Browser_type(UserBase):
#     browser_type:str


@router.post("/course_content", status_code=status.HTTP_201_CREATED)
async def register(user: UserBase):
    try:
        db = get_database()
        insert_query = course_content.insert().values(id=user.id,
                                                      name=user.name,
                                                      duration=user.duration,
                                                      course_id=user.course_id,
                                                      created_date=user.created_date,
                                                      updated_date=user.updated_date
                                                    )


        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')

@router.get("/course_content-data")
async def retrieve_course_content():
    select_stmt = course_content.select()
    result = await get_database().fetch_all(select_stmt)
    return result

@router.get("/course_content/{id}")
async def retrieve_individual_course_content(
    id: int

):
    select_stmt = course_content.select().where(course_content.c.id == id)
    result = await get_database().fetch_one(select_stmt)
    return result


#
# @router.post("/user_agent")
# async def browser_type(user_agent:str = Header(...)):
#     print(user_agent)
#     return{"user_agent":user_agent}
#     db = get_database()
#     insert_query = contact_form.insert().values(browser_type=user_agent.browser_type)
#     await db.execute(insert_query)
