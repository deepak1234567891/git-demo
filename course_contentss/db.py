import sqlalchemy
from databases import Database


DATABASE_URL = "sqlite:///course_content.db"
database = Database(DATABASE_URL)
sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)


def get_database() -> Database:
    return database