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

# how to run: poetry run python .\database_script.py

with Session(engine) as session:
   # сделать получение докторов без тикетов
   # перенести все SQL в код
    spec = 'Urolog'
   #  tickets = session.query(Ticket).join(Doctor).filter(Doctor.specialization == 'Urolog').all()
    # SELECT * FROM tickets JOIN doctors ON doctor_id = doctors.id WHERE "doctors"."specialization" = 'Urolog';
   #  doctors_ticket = session.query(Ticket).with_entities(func.count(Doctor.id), Doctor.name).join(Doctor).group_by(Doctor.id).all()
    # SELECT COUNT(doctor_id) as count, doctors.name FROM tickets JOIN doctors ON doctor_id = doctors.id GROUP BY "doctors"."id";
   #  doctors_3_tickets = session.query(Ticket).with_entities(func.count(Ticket.doctor_id), Doctor.name).join(Ticket.doctor).group_by(Doctor.id).having(func.count(Ticket.doctor_id) >= 3).all()
    # SELECT COUNT(doctor_id) as count, doctors.name FROM tickets JOIN doctors ON doctor_id = doctors.id GROUP BY "doctors"."id" HAVING tickets.count > 3;
   #  doctors_without_ticket = session.query(Doctor).outerjoin(Ticket).where(Ticket.id == None).all()
    #select * from doctors left join tickets on "tickets"."doctor_id" = "doctors"."id" where "tickets"."id" is null;
    update_doctor = session.execute(select(Doctor)
    .where(Doctor.id == "2")
    .values(specialization="Pulmonolog")    
    )
    # найти все тикеты конкретного доктора
    # напечатать их названия и Id
    # SQL
   #  print(tickets)
   #  print(doctors_ticket)
   #  print(doctors_3_tickets)
   #  print(doctors_without_ticket)
    print(update_doctor)
