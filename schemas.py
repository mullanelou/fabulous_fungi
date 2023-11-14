from fastapi import Form
from pydantic import BaseModel


# https://stackoverflow.com/a/60670614
class ContactUs(BaseModel):
    firstname: str
    lastname: str
    email: str
    message: str


    @classmethod
    def contact_us(
        contactform,
        firstname: str = Form(...),
        lastname: str = Form(...),
        email: str = Form(...),
        message: str = Form(...)
    ):
        return contactform(
            firstname=firstname,
            lastname=lastname,
            email=email,
            message=message
        )