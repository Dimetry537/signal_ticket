from dotenv import load_dotenv
import os
import asyncio

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import sessionmaker


load_dotenv('.env')
from sqlalchemy import create_engine, update
from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from models import Ticket
from models import Doctor 

import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# engine = create_engine(os.environ['DATABASE_URI'])

# # run sql in docker: docker-compose run --rm pg psql -U docker -h pg -d postgres
# # how to run: poetry run python .\database_script.py

# with Session(engine) as session:
#    # сделать получение докторов без тикетов
#    # перенести все SQL в код
#     # spec = 'Urolog'
   
#     # tickets = session.query(Ticket).join(Doctor).filter(Doctor.specialization == 'Urolog').all()
#     # # SELECT * FROM tickets JOIN doctors ON doctor_id = doctors.id WHERE "doctors"."specialization" = 'Urolog';
#     # print(tickets)

#     # doctors_ticket = session.query(Ticket).with_entities(func.count(Doctor.id), Doctor.name).join(Doctor).group_by(Doctor.id).all()
#     # # SELECT COUNT(doctor_id) as count, doctors.name FROM tickets JOIN doctors ON doctor_id = doctors.id GROUP BY "doctors"."id";
#     # print(doctors_ticket)

#     # doctors_3_tickets = session.query(Ticket).with_entities(func.count(Ticket.doctor_id), Doctor.name).join(Ticket.doctor).group_by(Doctor.id).having(func.count(Ticket.doctor_id) >= 3).all()
#     # # SELECT COUNT(doctor_id) as count, doctors.name FROM tickets JOIN doctors ON doctor_id = doctors.id GROUP BY "doctors"."id" HAVING tickets.count > 3;
#     # print(doctors_3_tickets)

#     # doctors_without_ticket = session.query(Doctor).outerjoin(Ticket).where(Ticket.id == None).all()
#     # #select * from doctors left join tickets on "tickets"."doctor_id" = "doctors"."id" where "tickets"."id" is null;
#     # print(doctors_without_ticket)

#     session.query(Doctor).filter(Doctor.id == "2").update({'specialization': "Pulmanolog"})
#     session.commit()
async def async_main():
    engine = create_async_engine(
        os.environ['DATABASE_URI'],
        echo=True,
    )
    # expire_on_commit=False will prevent attributes from being expired
    # after commit.
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        result = await session.execute(select(Doctor).where(Doctor.id==1))

        doctor = result.scalars().first()

        doctor.specialization = "Proctolog"

        await session.commit()

        stmt = select(Doctor).where(Doctor.id==1)

        result = await session.execute(stmt)
        print(result.scalars().first())

        # access attribute subsequent to commit; this is what
        # expire_on_commit=False allows
        print(doctor)

    # for AsyncEngine created in function scope, close and
    # clean-up pooled connections
    await engine.dispose()


asyncio.run(async_main())