import sqlalchemy
from datetime import datetime

metadata = sqlalchemy.MetaData()
course_content = sqlalchemy.Table(
    "course_content",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True,autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("duration", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("course_id", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=False)

)