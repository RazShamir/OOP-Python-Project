from datetime import datetime, timedelta
from book import Book
from customer import Customer
from loan import Loan
from library import Library


print("Welcome to the Library! what would you like to do?")
menu = ""
menu += "0. Reload menu\n"
menu += "1. Add new customer\n"
menu += "2. Add a book\n"
menu += "3. Loan a book\n"
menu += "4. Return a book\n"
menu += "5. Display all books\n"
menu += "6. Display all customers\n"
menu += "7. Display all loans\n"
menu += "8. Display all late loans\n"
menu += "9. Display loans for specific customer\n"
menu += "10. Find books by name\n"
menu += "11. Find books by author\n"
menu += "12. Find customer by name\n"
menu += "13. Remove a book from the Library\n"
menu += "14. Remove a customer from the Library\n"
menu += "15. Exit\n"
menu += "----------------------------------------"

lib = Library()

def op1():
    print("-Creat customer-")
    id: int = int(input("Customer ID: "))
    name = input("Customer name: ").capitalize()
    address = input("Customer address: ").capitalize()
    email = input("Customer Email: ")
    birth_date = input("Customer date of birth: ")
    customer = Customer(id, name, address, email, birth_date)
    lib.add_new_customer(customer)
    print("~Customer was succesfully added!~")
    
def op2():
    print("-Add book-")
    id = int(input("Book ID: "))
    name = input("Book name: ").capitalize()
    author = input("Book author: ").capitalize()
    year_published = input("Year published: ")
    type: int = int(input("Book loan type: "))
    book = Book(id, name, author, year_published, type)
    lib.add_new_book(book)
    print("~Book was succesfully added!~")

def op3():
    print("-Loan a book-")
    book_id: int = int(input("Book ID: "))
    customer_id: int = int(input("Customer ID: "))
    if lib.get_book_by_id(book_id) != None:
        if lib.get_customer_by_id(customer_id) != None:
            lib.loan_a_book(book_id, customer_id)
    print("~Enjoy your book!~")

def op4():
    print("-Return a book-")
    customer_id: int = int(input("Customer ID: "))
    if lib.get_customer_by_id(customer_id) != None:
        lib.return_book(customer_id)
    print("~The book has been returned to the Library!~")

def op5():
    lib.diasplay_book_list()

def op6():
    lib.display_customer_list()

def op7():
    lib.display_loan_list()

def op8():
    lib.display_late_loans()

def op9():
    print("-Who's loan are you looking for?-")
    customer_id: int = int(input("Customer ID: "))
    if lib.get_customer_by_id(customer_id) != None:
        lib.display_customer_loans(customer_id)

def op10():
    print("-Find a book-")
    book_name = input("Book name: ").capitalize()
    book = lib.get_book_by_name(book_name)
    if book != None:
        print(book)

def op11():
    print("-Find a book-")
    book_author = input("Book author: ").capitalize()
    book = lib.get_book_by_author(book_author)
    if book != None:
        print(book)

def op12():
    print("-Find customer-")
    customer_name = input("Customer name: ").capitalize()
    customer = lib.get_customer_by_name(customer_name)
    if customer != None:
        print(customer)

def op13():
    print("-Remove a book-")
    book_id: int = int(input("Book ID: "))
    book = lib.remove_book(book_id)
    if book != None:
        print(book)
    print("~The book has been removed from the Library~")

def op14():
    print("-Renove a customer-")
    customer_id: int = int(input("Customer ID: "))
    customer = lib.remove_customer(customer_id)
    if customer != None:
        print(customer)
    print("~The customer no longer exists in the Library database~")

def ticks():
    return (datetime.now() - datetime(1,1,1)).total_seconds()

def write_ex(ex):
    file_name = f"exceptions"
    with open(file_name, 'a') as f:
        f.write(str(ex) + "\n")

option = ""
print(menu)
while option != "15":
    try:
        option = input("Option: ")
        if option == "0":
            print(menu)
        if option == "1":
            op1()
        if option == "2":
            op2()
        if option == "3":
            op3()
        if option == "4":
            op4()
        if option == "5":
            op5()
        if option == "6":
            op6()
        if option == "7":
            op7()
        if option == "8":
            op8()
        if option == "9":
            op9()
        if option == "10":
            op10()
        if option == "11":
            op11()
        if option == "12":
            op12()
        if option == "13":
            op13()
        if option == "14":
            op14()
        if option == "15":
            print("Exiting Library, please come again!")
        if int(option) > 15 or int(option) < 0:
            raise ValueError("That is not an option!")
    except Exception as ex:
        print("ERROR: " + str(ex))
        write_ex(ex)
    if option != '15':
        print("What would you like to do now?")



#test notes:

