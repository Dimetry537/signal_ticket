from dotenv import load_dotenv
import os

load_dotenv('.env')
from sqlalchemy import create_engine
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
    # filter_by, order
    # найти все тикеты конкретного доктора
    # напечатать их названия и Id
    # SQL
    print(tickets)
    #print(doctor.name)
