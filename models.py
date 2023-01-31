import os
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime, date

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
Base  = declarative_base()

engine = create_async_engine(os.environ['DATABASE_URL'])

async_session = sessionmaker(engine, class_=AsyncSession)

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialization = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    tickets = relationship("Ticket", back_populates="doctor")

    def __repr__(self) -> str:
        return f"{self.name} | {self.specialization}"

def calculate_age(context):
    birthdate_date = context.get_current_parameters()["birthday"].isoformat()
    print(birthdate_date)
    born = datetime.strptime(birthdate_date[:10], '%Y-%m-%d')
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born, born.day))

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    birthday = Column(DateTime)
    diagnosis = Column(String)
    age = Column(Integer, default=calculate_age)
    # referral_clinic = Column()
    # self.ambulance_employee: Ambulance_employee = ambulance_employee
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    date_except = Column(DateTime)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    doctor = relationship('Doctor', back_populates="tickets")

    def __repr__(self) -> str:
        return f"{self.full_name} | {self.doctor_id}"