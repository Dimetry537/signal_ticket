from typing import List
from doctor import Doctor
from datetime import date
from datetime import datetime
from ambulance_operator import Ambulance_employee

class Ticket:
    def __init__(
        self,
        full_name: str,
        birthday: str,
        diagnosis: str,
        referral_clinic: str,
        age: int = None,
        date_of_the_ticket: date = None,
        ambulance_employee: Ambulance_employee = None, 
        doctor: Doctor = None, 
        date_except: date = None
    ) -> List:
        self.full_name = full_name
        self.birthday = birthday
        self.diagnosis = diagnosis
        self.age = age or self.__calculate_age(self.birthday)
        self.date = date_of_the_ticket or date.today()
        self.referral_clinic = referral_clinic
        self.ambulance_employee: Ambulance_employee = ambulance_employee
        self.doctor: Doctor = doctor
        self.date_except = date_except
    
    @classmethod
    def read_from_file(cls, filename, doctor: Doctor, ambulance_employee: Ambulance_employee):
        with open(filename, 'r', encoding="utf-8") as file:
            lines: List[str] = file.readlines()
            lines = list(map(lambda line: line[:len(line) - 1], lines))
            full_name = lines[0]
            birthday = lines[1]
            age = lines[2]
            date_of_the_ticket = lines[3]
            diagnosis = lines[4]
            referral_clinic = lines[5]
            date_except = lines[6]
            instance = cls(full_name, birthday, diagnosis, referral_clinic, age, date_of_the_ticket, ambulance_employee, doctor, date_except)
        return instance

    def ticket_in_work_by(self, doctor: Doctor) -> None:
        self.doctor = doctor
        self.date_except = date.today()

    def ambulance_in_work_by(self, ambulance_employee: Ambulance_employee) -> None:
        self.ambulance_employee = ambulance_employee
    
    def write_to_file(self, filename: str):
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(f'{self.full_name}\n{self.birthday}\n{self.age}\n{self.date}\n{self.diagnosis}\n{self.referral_clinic}\n{self.date_except}\n')
            
    def __calculate_age(self, bidthdate_date: str) -> int:
        born = datetime.strptime(bidthdate_date[:10], '%d.%m.%Y')
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born, born.day))

    def __repr__(self) -> List:
        return f"{self.full_name} | {self.birthday} | {self.age} | {self.date} | {self.diagnosis} | {self.referral_clinic} | {self.ambulance_employee} | {self.doctor} | {self.date_except}"

# class File:

#     def __init__(self, filename):
#         self.filename = filename
#         self.mode = 'a+'

#     def __enter__(self):
#         self.open_file = open(self.filename, self.mode)
#         return self.open_file

#     def __exit__(self, *args):
#         self.open_file.close()