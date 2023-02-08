from datetime import datetime

class Loan:
    def __init__(self, customer_id: int, book_id: int, loan_date: datetime, return_date: datetime) -> None:
        self._customer_id = customer_id
        self._book_id = book_id
        self._loan_date = loan_date
        self._return_date = return_date
    
    def get_customer_id(self):
        return self._customer_id
    
    def get_book_id(self):
        return self._book_id

    def get_loan_date(self):
        return self._loan_date
    
    def set_loan_date(self, date):
        self._loan_date = date
    
    def get_return_date(self):
        return self._return_date

    def set_return_date(self):
        return self._return_date
        
    def __str__(self) -> str:
        return f"Book-ID: {str(self.get_book_id())} Customer-ID: {str(self.get_customer_id())} Loan-Date: {self.get_loan_date()} Return-Date: {self.get_return_date()}"
    
    def __repr__(self) -> str:
        return self.__str__()