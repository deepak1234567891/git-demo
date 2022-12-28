from pydantic import BaseModel,EmailStr
from fastapi import status,APIRouter,HTTPException,Header
from datetime import datetime
from db import get_database
from models.course_category import course_category


router=APIRouter()


class UserBase(BaseModel):
    id: int
    name: str
    description: str
    created_date: datetime
    updated_date: datetime


# class Browser_type(UserBase):
#     browser_type:str


@router.post("/course_category", status_code=status.HTTP_201_CREATED)
async def register(user: UserBase):
    try:
        db = get_database()
        insert_query = course_category.insert().values(id=user.id,
                                                       name=user.name,
                                                       description=user.description,
                                                       created_date=user.created_date,
                                                       updated_date=user.updated_date
                                                      )


        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')

@router.get("/course_category-data")
async def retrieve_course_category():
    select_stmt = course_category.select()
    result = await get_database().fetch_all(select_stmt)
    return result

@router.get("/course_category/{id}")
async def retrieve_individual_course_category(
    id: int

):
    select_stmt = course_category.select().where(course_category.c.id == id)
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
