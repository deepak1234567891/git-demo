import sqlalchemy

# Creating a table
courses_metadata = sqlalchemy.MetaData()
courses = sqlalchemy.Table(
"courses",
courses_metadata,
sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
sqlalchemy.Column("title", sqlalchemy.String(length=50), nullable=True),
sqlalchemy.Column("course_description", sqlalchemy.String(length=1000), nullable=True),
sqlalchemy.Column("duration", sqlalchemy.Integer, nullable=True),
sqlalchemy.Column("language", sqlalchemy.String(length=50), nullable=True),
sqlalchemy.Column("course_classroom", sqlalchemy.String(length=255), nullable=True),
sqlalchemy.Column("created_date", sqlalchemy.Integer, nullable=True),
sqlalchemy.Column("updated_date", sqlalchemy.Integer, nullable=True)

)