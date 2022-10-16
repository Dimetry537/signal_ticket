import os
from pydoc import doc
from doctor import Doctor
from ticket import Ticket
from ambulance_operator import Ambulance_employee

doctor = Doctor('Maksakov M.D.', 'уролог')

ambulance_employee = Ambulance_employee('Сергеев А.В.', 'фельдшер', '52')

ticket = Ticket('Иванов И.И.', '01.01.1977', 'Пневмония', 'Поликлиника №1')

ticket_name = f"{ticket.date} {ticket.full_name} {ticket.age} лет.txt"

ticket.ambulance_in_work_by(ambulance_employee)

ticket.ticket_in_work_by(doctor)

doctor.write_to_file(f'{os.path.dirname(os.path.realpath(__file__))}/doctor.txt')

ambulance_employee.write_to_file(f'{os.path.dirname(os.path.realpath(__file__))}/ambulance_employee.txt')

ticket.write_to_file(f'{os.path.dirname(os.path.realpath(__file__))}/{ticket_name}')

filename_doctor = f'{os.path.dirname(os.path.realpath(__file__))}/doctor.txt'

filename_ambulance_employee = f'{os.path.dirname(os.path.realpath(__file__))}/ambulance_employee.txt'

filename = f'{os.path.dirname(os.path.realpath(__file__))}/{ticket_name}'

doctor_restored = Doctor.read_from_file(filename_doctor)

ambulance_employee_restored = Ambulance_employee.read_from_file(filename_ambulance_employee)

ticket_restored = Ticket.read_from_file(filename, doctor_restored, ambulance_employee)

print(ambulance_employee_restored)

print(doctor_restored)

print(ticket_restored)