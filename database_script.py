from dotenv import load_dotenv
import os

load_dotenv('.env')
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Ticket as ModelTicket
from models import Doctor as ModelDoctor

import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

engine = create_engine(os.environ['DATABASE_URI'])

with Session(engine) as session:
    doctor = session.query(ModelDoctor).first()
    # filter_by, order
    # найти все тикеты конкретного доктора
    # напечатать их названия и Id
    print(doctor.name)
    