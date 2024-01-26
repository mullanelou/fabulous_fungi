from fastapi import Form
from pydantic import BaseModel
from typing import Optional


# https://stackoverflow.com/a/60670614
#model vaildations - ensuring data from client side is same data type as field defined
class ContactUs(BaseModel):
    firstname: str
    lastname: str
    email: str
    message: str
    subscribe: bool = False

    @classmethod
    def contact_us(
        contactform,
        firstname: str = Form(...),
        lastname: str = Form(...),
        email: str = Form(...),
        message: str = Form(...),
        subscribe: Optional[str] = Form(None)
        
    ):
        subscribe_bool = True if subscribe=="true" else False
        return contactform(
            firstname=firstname,
            lastname=lastname,
            email=email,
            message=message,
            subscribe=subscribe_bool
            )

#Pydantic's orm_mode will instruct the Pydantic model to read the data as a dictionary and as an attribute
class Config:
    orm_mode = True


