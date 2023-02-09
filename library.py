from datetime import datetime, timedelta
from book import Book
from customer import Customer
from loan import Loan
import pickle
import os

class Library:
    def __init__(self) -> dict:
        self._customer_list: list[Customer] = []
        self._book_list: list[Book] = []
        self._loan_list: list[Loan] = []
        self._returned_loan_list: list[Loan] = []
        self.load()

    def save(self):
        data = [self._customer_list, self._book_list, self._loan_list, self._returned_loan_list]
        with open("libraryDB.pickle", 'wb') as f:
            pickle.dump(data, f)

    def load(self):
        if os.path.exists("libraryDB.pickle") == False:
            return

        with open("libraryDB.pickle", 'rb') as f:
            data = pickle.load(f)
            self._customer_list = data[0]
            self._book_list = data[1]
            self._loan_list = data[2]
            self._returned_loan_list = data[3]
    
    def add_new_customer(self, customer: Customer):
        for cus in self._customer_list:
            if cus.get_id() == customer.get_id():
                raise ValueError("Customer already exists")
        self._customer_list.append(customer)
        self.save()
    
    def add_new_book(self, book: Book):
        for bk in self._book_list:
            if bk.get_id() == book.get_id():
                raise ValueError("Book already exists")
        self._book_list.append(book)
        self.save()

    def get_book_by_id(self,book_id: int):
        for book in self._book_list:
            if book.get_id() == book_id:
                return book
        raise ValueError("Book id doesn't exist")

    def loan_a_book(self, book_id: int, customer_id: int):
        for loan in self._loan_list:
            if customer_id == loan.get_customer_id():
                if loan.get_return_date() == None:
                    raise ValueError("Customer has not returned last loan")

            if book_id == loan.get_book_id():
                raise ValueError("The book is already loaned")
        
        last_loan = None
        for loan in self._returned_loan_list:
            if loan.get_customer_id() == customer_id:
                if last_loan == None:
                    last_loan = loan
                else:
                    if loan.get_loan_date() > last_loan.get_loan_date():
                        last_loan = loan
        if last_loan != None:
            book = self.get_book_by_id(book_id)
            if last_loan.get_return_date() - last_loan.get_loan_date() >= book.get_loan_time():
                if last_loan.get_return_date() + timedelta(weeks=2) > datetime.now():
                    raise ValueError("Client is in a 2 weeks ban")
                else:
                    print("Two weeks have passed, the client is no longer baned")

        new_loan = Loan(customer_id, book_id, datetime.now(), None)
        self._loan_list.append(new_loan)
        self.save()
    
    def diasplay_book_list(self):
        print(f"List of books: {self._book_list}")
    
    def display_customer_list(self):
        print(f"List of customers: {self._customer_list}")
    
    def display_loan_list(self):
        print(f"List of loans: {self._loan_list}")

    def get_book_by_loan(self, loan: Loan) -> Book:
        for book in self._book_list:
            if book.get_id() == loan.get_book_id():
                return book
        
        raise ValueError("The book hasn't been loaned")
    
    def get_late_loans(self): #loans were not returned yet
        late_loans_list: list[Loan] = []
        for loan in self._loan_list:
            book: Book = self.get_book_by_loan(loan)
            if datetime.now() > loan._loan_date + book.get_loan_time():
                late_loans_list.append(loan)
        return late_loans_list

    def display_late_loans(self):
        late_loans_list: list[Loan] = self.get_late_loans()
        print(f"List of late loans: {late_loans_list}")
    
    def display_customer_loans(self, customer_id: int):
        customer_loans_list: list[Loan] = []
        customer = self.get_customer_by_id(customer_id)
        for loan in self._loan_list:
            if loan.get_customer_id() == customer_id:
                customer_loans_list.append(loan)
        print(f"{customer.get_name()}'s loans: {customer_loans_list}")
    
    def get_book_by_name(self, book_name: str):
        books: list[Book] = []
        for bk in self._book_list:
            if book_name.lower() in bk.get_name().lower():
                books.append(bk)
        if books == []:
            raise ValueError("Book name doesn't exist")
        else:
            return books
        
    def get_book_by_author(self, book_author: str):
        books: list[Book] = []
        for bk in self._book_list:
            if book_author.lower() in bk.get_author().lower():
                books.append(bk)
        if books == []:
            raise ValueError("Book author doesn't exist")
        else:
            return books
    
    def get_customer_by_name(self, customer_name: str):
        for cus in self._customer_list:
            if customer_name.lower() in cus.get_name().lower():
                return cus
        raise ValueError("Customer does't exist")

    def get_customer_by_id(self, customer_id: str):
        for cus in self._customer_list:
            if customer_id == cus.get_id():
                return cus
        raise ValueError("Customer does't exist")
    
    def get_loan_by_books(self, book: Book) -> Loan:
        for loan in self._loan_list:
            if loan.get_book_id() == book.get_id():
                return loan
        
        return None

    def remove_book(self, book_id: int):
        for bk in self._book_list:
            if bk.get_id() == book_id:
                if self.get_loan_by_books(bk) == None:
                    self._book_list.remove(bk)
                    self.save()
                    return
                else:
                    raise ValueError("Book is already loaned")

        raise ValueError("Book doesn't exist")
    
    def get_loan_by_customer(self, customer: Customer):
        for loan in self._loan_list:
            if loan.get_customer_id() == customer.get_id():
                return loan
            
        return None
    
    def remove_customer(self, customer_id: int):
        for cus in self._customer_list:
            if cus.get_id() == customer_id:
                if self.get_loan_by_customer(cus) == None:
                    self._customer_list.remove(cus)
                    self.save()
                    return
                else:
                    raise ValueError("Customer has loaned books")

        raise ValueError("Customer doesn't exist")

    def return_book(self, customer_id : int):
        customer: Customer = self.get_customer_by_id(customer_id)
        loan: Loan = self.get_loan_by_customer(customer)
        if loan == None:
            raise ValueError("This book is not loaned")
        else:
            if loan in self.get_late_loans():
                print("The customer has not returned his book on time, he cannot loan for 2 weeks")
            
            loan._return_date = datetime.now()
            self._returned_loan_list.append(loan)
            self._loan_list.remove(loan)
            self.save()
    
    #unused
    def get_late_returned(self):
        late_list: list[Loan] = []
        for loan in self._returned_loan_list:
            book = self.get_book_by_id(loan.get_book_id())
            if loan.set_return_date() - loan.get_loan_date() >= book.get_loan_time():
                late_list.append(loan)
        return late_list



        
        
