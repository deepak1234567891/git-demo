from pydantic import BaseModel,EmailStr
from fastapi import status,APIRouter,HTTPException,Header
from datetime import datetime
from db import get_database
from models.contact_form import contact_form


router=APIRouter()


class UserBase(BaseModel):
    id: int
    name: str
    mobile: str
    email: EmailStr
    message: str
    created_date: datetime
    browser_type: str

# class Browser_type(UserBase):
#     browser_type:str


@router.post("/contact_form", status_code=status.HTTP_201_CREATED)
async def register(user: UserBase):
    try:
        db = get_database()
        insert_query = contact_form.insert().values(id=user.id,
                                                    name=user.name,
                                                    mobile=user.mobile,
                                                    email=user.email,
                                                    message=user.message,
                                                    created_date=user.created_date,
                                                    browser_type=user.browser_type
                                                    )

        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')

@router.get("/contact_form-data")
async def retrieve_contact_form():
    select_stmt = contact_form.select()
    result = await get_database().fetch_all(select_stmt)
    return result

@router.get("/contact_form/{id}")
async def retrieve_individual_contact_form(
    id: int

):
    select_stmt = contact_form.select().where(contact_form.c.id == id)
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
