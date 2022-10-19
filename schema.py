# build a schema using pydantic
from datetime import datetime
from pydantic import BaseModel

class Ticket(BaseModel):
    full_name: str
    birthday: datetime
    diagnosis: str
    # referral_clinic = Column()
    # self.ambulance_employee: Ambulance_employee = ambulance_employee
    doctor_id: int

    class Config:
        orm_mode = True

class Doctor(BaseModel):
    name: str
    specialization: str

    class Config:
        orm_mode = True
        