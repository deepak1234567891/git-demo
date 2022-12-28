import sqlalchemy
from datetime import datetime

metadata = sqlalchemy.MetaData()
mentors = sqlalchemy.Table(
    "mentors",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, autoincrement=True),
    sqlalchemy.Column("mentor_id", sqlalchemy.Integer,  autoincrement=True),
    sqlalchemy.Column("first_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("middle_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("last_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("email", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("education", sqlalchemy.String(length=10), nullable=True),
    sqlalchemy.Column("years_of_experience", sqlalchemy.Integer, nullable=True),
    # sqlalchemy.Column("photo", sqlalchemy.File, nullable=True),
    # sqlalchemy.Column("gender", sqlalchemy.enum, nullable=True),
    sqlalchemy.Column("marital_status", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("comm_addr1", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("comm_addr2", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("comm_addr3", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("comm_city", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("comm_state", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("comm_country", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("comm_mobile", sqlalchemy.Integer, nullable=True),
    sqlalchemy.Column("comm_landmark", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("perm_addr1", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("perm_addr2", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("perm_addr3", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("perm_city", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("perm_state", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_country", sqlalchemy.String(length=20), nullable=True),
    sqlalchemy.Column("alternate_mobile", sqlalchemy.Integer, nullable=True),
    sqlalchemy.Column("perm_landmark", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=True)
)

