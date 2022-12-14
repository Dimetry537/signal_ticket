from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime, date

Base  = declarative_base()

def calculate_age(context):
    bidthdate_date = context.get_current_parameters()["birthday"]
    born = datetime.strptime(bidthdate_date[:10], '%d.%m.%Y')
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born, born.day))

class Ticket(Base):
    __tablename__ = 'tickets'
    id  = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    birthday = Column(DateTime)
    diagnosis = Column(String)
    age = Column(Integer, default=calculate_age)
    # referral_clinic = Column()
    # self.ambulance_employee: Ambulance_employee = ambulance_employee
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    date_except = Column(DateTime)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    # doctor = relationship('doctors')


class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialization = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

