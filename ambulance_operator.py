#создать оператора СМП, подстанция, специализация
#поликлинка в которую направляем пациента

from typing import List

class Ambulance_employee:
    def __init__(self, employee_name: str, specialization: str, brigade_number: str):
        self.employee_name = employee_name
        self.specialization = specialization
        self.brigade_number = brigade_number

    @classmethod
    def read_from_file(cls, filename):
        with open(filename, 'r', encoding="utf-8") as file:
            lines: List[str] = file.readlines()
            lines = list(map(lambda line: line[:len(line) - 1], lines))
            employee_name = lines[0]
            specialization = lines[1]
            brigade_number = lines[2]
            instance = cls(employee_name, specialization, brigade_number)
        return instance
        
    def write_to_file(self, filename: str):
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(f'{self.employee_name}\n{self.specialization}\n{self.brigade_number}\n')
                
    def __repr__(self) -> List:
         return f"{self.employee_name} | {self.specialization} | {self.brigade_number}"