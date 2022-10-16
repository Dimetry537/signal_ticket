from typing import List

class Doctor:
    def __init__(self, doctor_name: str, specialization: str):
        self.doctor_name = doctor_name
        self.specialization = specialization

    @classmethod
    def read_from_file(cls, filename):
        with open(filename, 'r', encoding="utf-8") as file:
            lines: List[str] = file.readlines()
            lines = list(map(lambda line: line[:len(line) - 1], lines))
            doctor_name = lines[0]
            specialization = lines[1]
            instance = cls(doctor_name, specialization)
        return instance
        
    def write_to_file(self, filename: str):
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(f'{self.doctor_name}\n{self.specialization}\n')
                
    def __repr__(self) -> List:
         return f"{self.doctor_name} | {self.specialization}"