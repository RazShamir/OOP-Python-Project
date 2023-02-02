from datetime import datetime, timedelta

class Book():
    def __init__(self, id : int, name : str, author : str, year_published : datetime, type: str ) -> None:
        self._id = id
        self._name = name
        self._author = author
        self._year_published = year_published
        self._type = type
    
    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    def get_author(self):
        return self._author
    
    def get_year_published(self):
        return self._year_published
    
    def set_type(self, loan_type: str):
        self._type = loan_type

    def get_loan_time(self) -> timedelta:
        if self._type == '1':
            return timedelta(days=10)
        elif self._type == '2':
            return timedelta(days=5)
        elif self._type == '3':
            return timedelta(days=2)
        else:
            raise ValueError("Book type cannot be " + self._type)



