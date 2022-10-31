from dotenv import load_dotenv

load_dotenv('.env')

import os
from fastapi import FastAPI, HTTPException
from doctor import Doctor
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import Ticket as SchemaTicket
from schema import Doctor as SchemaDoctor

from schema import Ticket
from schema import Doctor

from models import Ticket as ModelTicket
from models import Doctor as ModelDoctor

import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

#*ошибка, что такого доктора нет
#get на ticket и put (обновление ticket) * получение доктора и дополнение SQL alchemy update model
#валидация

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URI'])

@app.post('/ticket/', response_model=SchemaTicket)
async def create_ticket(ticket: SchemaTicket):
    doctor = db.session.query(ModelDoctor).filter_by(id=id).first()
    if ticket.doctor_id not in doctor:
        raise HTTPException(status_code=404, detail="doctor not found")
    #создать такого доктора нет
    db_ticket = ModelTicket(
        full_name=ticket.full_name, 
        birthday=ticket.birthday,
        diagnosis=ticket.diagnosis, 
        doctor_id=ticket.doctor_id
    )
    db.session.add(db_ticket)
    db.session.commit()
    db.session.refresh(db_ticket)
    return db_ticket

@app.get("/doctors/{id}", response_model=SchemaDoctor)
async def show_doctor(id):
    doctor = db.session.query(ModelDoctor).filter_by(id=id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail='Такого доктора не существует')
    return doctor

@app.post('/doctors/', response_model=SchemaDoctor)
async def create_doctor(doctor: SchemaDoctor):
    db_doctor = ModelDoctor(name=doctor.name, specialization=doctor.specialization)
    db.session.add(db_doctor)
    db.session.commit()
    db.session.refresh(db_doctor)
    return db_doctor
<<<<<<< HEAD
    
=======

#1
>>>>>>> 93516dc (new pull request)
