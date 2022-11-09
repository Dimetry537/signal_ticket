from typing import List
from dotenv import load_dotenv

load_dotenv('.env')

import os
from fastapi import FastAPI, HTTPException
from doctor import Doctor
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import TicketParams
from schema import DoctorParams, DoctorResponse

from models import Ticket
from models import Doctor

import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

#*ошибка, что такого доктора нет
#get на ticket и put (обновление ticket) * получение доктора и дополнение SQL alchemy update model
#валидация

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URI'])

@app.post('/tickets', response_model=TicketParams)
async def create_ticket(ticket: TicketParams):
    # select * from doctors where  id =ticket.doctor_id
    doctor = db.session.query(Doctor).filter_by(id=ticket.doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail='Такого доктора не существует')
    db_ticket = Ticket(
        full_name=ticket.full_name,
        birthday=ticket.birthday,
        diagnosis=ticket.diagnosis,
        doctor_id=ticket.doctor_id
    )
    db.session.add(db_ticket)
    db.session.commit()
    db.session.refresh(db_ticket)
    return db_ticket

@app.get("/tickets", response_model=List[TicketParams])
async def index_tickets():
    tickets = db.session.query(Ticket).all()
    return tickets

@app.get("/tickets/{id}", response_model=List[TicketParams])
async def show_ticket(id):
    ticket = db.session.query(Ticket).filter_by(id=id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail='Такого ticket не существует')
    return ticket


@app.get("/doctors/{id}", response_model=DoctorResponse)
async def show_doctor(id):
    doctor = db.session.query(Doctor).filter_by(id=id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail='Такого доктора не существует')
    return doctor

@app.get("/doctors", response_model=List[DoctorResponse])
async def index_doctor():
    doctors = db.session.query(Doctor).all()
    return doctors

@app.get("/doctors/{doctor_id}/tickets", response_model=List[TicketParams])
async def index_tickets(doctor_id):
    tickets = db.session.query(Ticket).filter(Ticket.doctor_id == doctor_id).all()
    if not tickets:
        raise HTTPException(status_code=404, detail='Такого талона не существует')
    return tickets

    # 1) SOAP - xml - Java 99%, C#
    # 2) JSON - 99%
    # {
    #     "key": "value",
    #     "key1": {
    #         "key": "value"
    #     }
    # }
    # REST - https://ru.wikipedia.org/wiki/REST
    # JSONAPI - https://jsonapi.org/
    # JSON -
    # GraphQL
    # 3) binary - rpc, grpc - https://en.wikipedia.org/wiki/GRPC

@app.post('/doctors', response_model=DoctorResponse)
async def create_doctor(doctor: DoctorParams):
    db_doctor = Doctor(name=doctor.name, specialization=doctor.specialization)
    db.session.add(db_doctor)
    db.session.commit()
    db.session.refresh(db_doctor)
    return db_doctor
