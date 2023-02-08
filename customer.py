from datetime import datetime

class Customer:
    def __init__(self, id: int, name: str, address: str, email: str, birth_date: datetime) -> None:
        self._id = id
        self._name = name
        self._address = address
        self._email = email
        self._birth_date = birth_date
    
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
    
    def get_address(self):
        return self._address
    
    def get_email(self):
        return self._email
    
    def get_birth_date(self):
        return self._birth_date

    def __str__(self) -> str:
        return f"ID: {str(self.get_id())} Name: {self.get_name()} Address: {self.get_address()} Email: {self.get_email()} Birthdate: {self.get_birth_date()}"

    def __repr__(self) -> str:
        return self.__str__()