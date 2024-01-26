from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Boolean
from database import Base

class Subscribers(Base):
    __tablename__ = "subscribers"

    id = Column(Integer, primary_key=True, index=True) 
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)



