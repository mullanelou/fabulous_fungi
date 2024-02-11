# The functionality for your API is provided by the FastAPI Python class.

from typing import Any
from unicodedata import name
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from model import Subscribers, Base
from schema import ContactUs
from sqlalchemy.orm import Session
import ssl
import smtplib
from email.message import EmailMessage

app = FastAPI()  # creates the fastAPI instance

# creates all table objects, in this case one Newsletter table
Base.metadata.create_all(bind=engine)

# create and close the session


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app.mount("/images", StaticFiles(directory="templates/images"), name="images")
app.mount("/css", StaticFiles(directory="templates/css"), name="css")
app.mount("/js", StaticFiles(directory="templates/js"), name="js")
app.mount("/bootstrap-5.3.1-dist",
          StaticFiles(directory="templates/bootstrap-5.3.1-dist"), name="bootstrap-5.3.1-dist")
app.mount("/webfonts", StaticFiles(directory="templates/webfonts"), name="webfonts")

templates = Jinja2Templates(directory="templates")

# @app.get("/") This is a python decorator that specifies to FastAPI that the function below it is in charge of request handling.
# / This is a decorator that specifies the route. This creates a GET method on the sites route. The result is then returned by the wrapped function.


@app.get('/Fungi_Index.html', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("Fungi_Index.html", {"request": request})


@app.get('/About.html', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("About.html", {"request": request})


@app.get('/Facts.html', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("Facts.html", {"request": request})


@app.get('/ContactUs.html', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("ContactUs.html", {"request": request})


@app.get('/ContactUsreturn.html', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("ContactUsreturn.html", {"request": request})


@app.get('/subscribed.html', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("subscribed.html", {"request": request})


@app.post('/ContactUs', response_class=HTMLResponse)
async def create_subscriber(request: Request, db: Session = Depends(get_database_session), form_data: ContactUs = Depends(ContactUs.contact_us)):
    if form_data.subscribe == True:
        monthly_news = Subscribers(
            firstname=form_data.firstname, lastname=form_data.lastname, email=form_data.email)
        db.add(monthly_news)
        db.commit()
        return templates.TemplateResponse("subscribed.html", {"request": request})

    else :
        email_address = "makeitsewclass@gmail.com" # type Email
        email_password = "hhfo gewf atoh bshk" # If you do not have a gmail apps password, create a new app with using generate password. Check your apps and passwords https://myaccount.google.com/apppasswords 
        #Must set up 2 step verification on email address first then can generate 16 code password to allow email being sent from gmail server
 
        # create email
        msg = EmailMessage()
        msg['Subject'] = "Message from Fabulous Fungi Website"
        msg['From'] = email_address
        msg['To'] = "mullanelou@gmail.com" # type Email
        msg.set_content(
        
        f"""   \
        Name : {form_data.firstname, form_data.lastname}
        Email : {form_data.email}
        Message : {form_data.message}
        """ ,
        ) #triple quotes allows you to write multple lines

        context = ssl.create_default_context() #standard email encryption security

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
            smtp.quit() #Terminate the SMTP session and close the connection

        return templates.TemplateResponse("ContactUsreturn.html", {"request": request})


"""@app.post('/ContactUs', response_class=HTMLResponse)
async def contactus_form(request: Request, form_data: ContactUs = Depends(ContactUs.contact_us), db: Session = Depends(get_database_session)):

    print(form_data)

    if form_data.subscribe == True: 
        #async def create_news(request: Request, db:Session = Depends(get_database_session)):
            monthly_news = Subscribers(firstname=form_data.firstname, lastname=form_data.lastname, email=form_data.email)
            db.add(monthly_news)
            db.commit()
    return templates.TemplateResponse("subscribed.html", {"request": request})
    
    else :

        email_address = "makeitsewclass@gmail.com" # type Email
        email_password = "hhfo gewf atoh bshk" # If you do not have a gmail apps password, create a new app with using generate password. Check your apps and passwords https://myaccount.google.com/apppasswords 
        #Must set up 2 step verification on email address first then can generate 16 code password to allow email being sent from gmail server
 
        # create email
        msg = EmailMessage()
        msg['Subject'] = "Message from Fabulous Fungi Website"
        msg['From'] = email_address
        msg['To'] = "mullanelou@gmail.com" # type Email
        msg.set_content(
        
        f"""  # \
# Name : {form_data.firstname, form_data.lastname}
# Email : {form_data.email}
# Message : {form_data.message}
""" ,

    ) #triple quotes allows you to write multple lines

    context = ssl.create_default_context() #standard email encryption security

    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        smtp.quit() #Terminate the SMTP session and close the connection

return templates.TemplateResponse("ContactUsreturn.html", {"request": request}) """
