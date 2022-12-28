import sqlalchemy
from datetime import datetime

metadata = sqlalchemy.MetaData()
course_category = sqlalchemy.Table(
    "course_category",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("description", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("created_date", sqlalchemy.Date, nullable=True),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=True)

)