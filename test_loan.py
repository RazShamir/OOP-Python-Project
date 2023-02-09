import unittest
from library import Library
from book import Book
from customer import Customer
from loan import Loan
from datetime import datetime, timedelta
import os

def clear_database():
        if os.path.exists("libraryDB.pickle"):
            os.remove("libraryDB.pickle")

class LibraryTest(unittest.TestCase):
    def __init__(self):
        clear_database()
        self.lib = Library()
    
    def create_customer(self):
        cus = Customer(123, "raz", "add", "gmail", "5,5,2000")
        self.lib.add_new_customer(cus)

    def create_book(self):
        bk = Book(234, "bk", "auth", "1990", 1)
        self.lib.add_new_book(bk)

    def loan_book(self, when: datetime = datetime.now()):
        self.lib.loan_a_book(234, 123)
        cus = self.lib.get_customer_by_id(123)
        loan = self.lib.get_loan_by_customer(cus)
        loan._loan_date = when
        self.assertGreater(len(self.lib._loan_list), 0)
        

    def return_book(self, when: datetime = datetime.now()):
        cus = self.lib.get_customer_by_id(123)
        loan = self.lib.get_loan_by_customer(cus)
        self.lib.return_book(123)
        loan._return_date = when

try:
    test = LibraryTest()
    lib = test.lib
    test.create_customer()
    test.create_book()

    test.loan_book( datetime.now() - timedelta(days=30) )
    test.return_book(datetime.now() - timedelta(days=15) )


    test.loan_book(datetime.now() - timedelta(days=14))
    test.return_book()
    test.loan_book()


except Exception as ex:
    print(str(ex))
