from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#ORM Object Relational Mapper

# localhost
# DATABASE_URL = "postgresql://louisemullane:DataBa5e!@localhost:5432/mydb"

# mydb.cz28s8woidtp.eu-north-1.rds.amazonaws.com
DATABASE_URL = "postgresql://louisemullane:DataBa5e!@mydb.cz28s8woidtp.eu-north-1.rds.amazonaws.com:5432/mydb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
