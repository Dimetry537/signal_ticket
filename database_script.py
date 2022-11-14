from dotenv import load_dotenv
import os

load_dotenv('.env')
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from models import Ticket
from models import Doctor 

import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

engine = create_engine(os.environ['DATABASE_URI'])

with Session(engine) as session:
   # сделать получение докторов без тикетов
   # перенести все SQL в код
    spec = 'Urolog'
    tickets = session.query(Ticket).join(Ticket.doctor).filter(Doctor.specialization == 'Urolog').all()
    # SELECT * FROM tickets JOIN doctors ON doctor_id = doctors.id WHERE "doctors"."specialization" = 'Urolog';
    doctors_ticket = session.query(Ticket, Doctor.name).join(Ticket.doctor).group_by(Doctor.id).count(Ticket.doctor_id)
    # SELECT COUNT(doctor_id) as count, doctors.name FROM tickets JOIN doctors ON doctor_id = doctors.id GROUP BY "doctors"."id";
    doctors_3_tickets = session.query(Ticket, Doctor.name).join(Ticket.doctor).group_by(Doctor.id).having(func.count(Ticket.doctor_id) > 3)
    # SELECT COUNT(doctor_id) as count, doctors.name FROM tickets JOIN doctors ON doctor_id = doctors.id GROUP BY "doctors"."id" HAVING tickets.count > 3;
    doctors_without_ticket = session.query(Doctor, Ticket).outerjoin(Ticket.doctor_id == Doctor.id).where(Ticket.doctor_id == None)
    #select * from doctors left join tickets on "tickets"."doctor_id" = "doctors"."id" where "tickets"."doctor_id" is null;
    # найти все тикеты конкретного доктора
    # напечатать их названия и Id
    # SQL
    print(f'{tickets} /n{doctors_ticket} /n{doctors_3_tickets} /n{doctors_without_ticket}')
    #print(doctor.name)
