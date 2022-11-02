# build a schema using pydantic
from datetime import datetime
from pydantic import BaseModel

class TicketParams(BaseModel):
    full_name: str
    birthday: datetime
    diagnosis: str
    # referral_clinic = Column()
    # self.ambulance_employee: Ambulance_employee = ambulance_employee
    doctor_id: int

    class Config:
        orm_mode = True

class DoctorResponse(BaseModel):
    name: str
    specialization: str
    time_created: datetime
    time_updated: datetime | None

    class Config:
        orm_mode = True

class DoctorParams(BaseModel):
    name: str
    specialization: str

    class Config:
        orm_mode = True
