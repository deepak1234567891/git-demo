from pydantic import BaseModel,EmailStr
from fastapi import status,APIRouter,HTTPException
from datetime import datetime
from db import get_database
from models.mentors import mentors


router=APIRouter()


class UserBase(BaseModel):
    id: int
    mentor_id: int
    first_name: str
    middle_name: str
    last_name: str
    email: EmailStr
    education: str
    years_of_experience: int
    # photo: File
    # gender: enum
    marital_status: str
    comm_addr1: str
    comm_addr2: str
    comm_addr3: str
    comm_city: str
    comm_state: str
    comm_country: str
    comm_mobile: int
    comm_landmark: str
    perm_addr1: str
    perm_addr2: str
    perm_addr3: str
    perm_city: str
    perm_state: str
    perm_country: str
    alternate_mobile: int
    perm_landmark: str
    created_date: datetime
    updated_date: datetime


# class Browser_type(UserBase):
#     browser_type:str

@router.post("/mentors", status_code=status.HTTP_201_CREATED)
async def register(user: UserBase):
    try:
        db = get_database()
        insert_query = mentors.insert().values(id=user.id,
                                                    mentor_id=user.mentor_id,
                                                    first_name=user.first_name,
                                                    middle_name=user.middle_name,
                                                    last_name=user.last_name,
                                                    email=user.EmailStr,
                                                    education=user.education,
                                                    years_of_experience=user.years_of_experience,
                                                    # photo=user.photo,
                                                    # gender=user.gender,
                                                    marital_status=user.marital_status,
                                                    comm_addr1=user.comm_addr1,
                                                    comm_addr2=user.comm_addr2,
                                                    comm_addr3=user.comm_addr3,
                                                    comm_city= user.comm_city,
                                                    comm_state=user.comm_state,
                                                    comm_country=user.comm_country,
                                                    comm_mobile=user.comm_mobile,
                                                    comm_landmark=user.comm_landmark,
                                                    perm_addr1=user.perm_addr1,
                                                    perm_addr2=user.perm_addr2,
                                                    perm_addr3=user.perm_addr3,
                                                    perm_city= user.perm_city,
                                                    perm_state=user.perm_state,
                                                    perm_country=user.perm_country,
                                                    alternate_mobile=user.alternate_mobile,
                                                    perm_landmark=user.perm_landmark,
                                                    created_date=user.created_date,
                                                    updated_date=user.updated_date
                                               )


        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')





@router.get("/mentors-data")
async def retrieve_mentors():
    select_stmt = mentors.select()
    result = await get_database().fetch_all(select_stmt)
    return result

@router.get("/mentors/{id}")
async def retrieve_individual_contact_form(
     id: int

):
     select_stmt = mentors.select().where(mentors.c.id == id)
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
