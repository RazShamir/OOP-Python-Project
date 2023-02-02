from datetime import datetime
from book import Book
from customer import Customer
from loan import Loan

class Library:
    def __init__(self) -> dict:
        self._customer_list: list[Customer] = []
        self._book_list: list[Book] = []
        self._loan_list: list[Loan] = []
    
    def add_new_customer(self, customer: Customer):
        for cus in self._customer_list:
            if cus.get_id() == customer.get_id():
                raise ValueError("Customer already exists")
        self._customer_list.append(customer)
    
    def add_new_book(self, book: Book):
        for bk in self._book_list:
            if bk.get_id() == book.get_id():
                raise ValueError("Book already exists")
        self._book_list.append(book)
    
    def loan_a_book(self, loan: Loan, book: Book):
        if loan in self._loan_list:
            raise ValueError("The book is already loaned")
        for bk in self._book_list:
            if bk.get_id() == book.get_id():
                self._loan_list.append(loan)
    
    def diasplay_book_list(self):
        print(f"List of books: {self._book_list}")
    
    def display_customer_list(self):
        print(f"List of customers: {self._customer_list}")
    
    def display_loan_list(self):
        print(f"List of loans: {self._loan_list}")

    def get_book_by_loan(self, book: Book, loan: Loan) -> Book:
        for book in self._book_list:
            if book.get_id() == loan.get_book_id():
                return book
        
        raise ValueError("The book hasn't been loaned")
    
    def display_late_loans(self):
        late_loans_list: list[Loan] = []
        for loan in self._loan_list:
            book: Book = self.get_book_by_loan(loan)
            if datetime.now() > loan._loan_date + book.get_loan_time():
                late_loans_list.append(loan)
        print(f"List of late loans: {late_loans_list}")
    
    def display_customer_loans(self, customer: Customer):
        customer_loans_list: list[Loan] = []
        for loan in self._loan_list:
            if loan.get_customer_id() == customer.get_id():
                customer_loans_list.append(loan)
        print(f"The customers loans: {customer_loans_list}")
    
    def get_book_by_name(self, bookName: str):
        books: list[Book] = []
        for bk in self._book_list:
            if bookName in bk.get_name():
                books.append(bk)
        if books == []:
            raise ValueError("Book name doesn't exist")
        else:
            return books
        
    def get_book_by_author(self, bookAuthor: str):
        books: list[Book] = []
        for bk in self._book_list:
            if bookAuthor in bk.get_author():
                books.append(bk)
        if books == []:
            raise ValueError("Book author doesn't exist")
        else:
            return books
    
    def get_customer_by_name(self, customer_name: str):
        for cus in self._customer_list:
            if customer_name in cus.get_name():
                return customer_name
        raise ValueError("Customer does't exist")
    
    def get_loan_by_books(self, book: Book) -> Loan:
        for loan in self._loan_list:
            if loan.get_book_id() == book.get_id():
                return loan
        
        raise None

    def remove_book(self, bookId: int):
        for bk in self._book_list:
            if bk.get_id() == bookId:
                if self.get_loan_by_books(bk) == None:
                    self._book_list.remove(bk)
                    return
                else:
                    raise ValueError("Book is already loaned")
        
        raise ValueError("Book doesn't exist")


        
        
