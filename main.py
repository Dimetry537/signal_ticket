from dotenv import load_dotenv

load_dotenv('.env')

import os
from fastapi import FastAPI
from doctor import Doctor
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import Ticket as SchemaTicket
from schema import Doctor as SchemaDoctor

from schema import Ticket
from schema import Doctor

from models import Ticket as ModelTicket
from models import Doctor as ModelDoctor

#сделать Ticket так же как Doctors, надо чтобы выдавалась *ошибка, что такого доктора нет

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URI'])

@app.post('/ticket/', response_model=SchemaTicket, response_model=SchemaDoctor)
async def create_ticket(ticket: SchemaTicket):
    db_ticket = ModelTicket(full_name=ticket.full_name, birthday=ticket.birthday, diagnosis=ticket.diagnosis, doctor_id=Doctor.name)
    db.session.add(db_ticket)
    db.session.commit()
    db.session.refresh(db_ticket)
    return db_ticket

@app.post('/doctors/', response_model=SchemaDoctor)
async def create_doctor(doctor: SchemaDoctor):
    db_doctor = ModelDoctor(name=doctor.name, specialization=doctor.specialization)
    db.session.add(db_doctor)
    db.session.commit()
    db.session.refresh(db_doctor)
    return db_doctor

@app.get("/doctor")
async def read_doctor():
    doctor = db.session.query(ModelDoctor).first()
    return doctor