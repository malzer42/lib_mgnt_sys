"""Driver for the LMIS."""
# Author(s): Pierre Abraham Mulamba
# Date of creation (modification): 20200224 (20200224)

import time
import random


from book import Book
from borrow import Borrow
from library import Library
from subscriber import Subscriber


def main():
    """
    The main controller for the LMIS.
    Used to create instances of different classes
    Used for integration testing and various implemented methods

    """
    start_time = time.time()
    print("IF YOU FAIL TO PLAN FOR FAILURES, YOU ARE PLANNING TO FAIL AS AN SQA.")

    try:
        print("LIBRARY MANAGEMENT INVENTORY SYSTEM")
        print("INTEGRATION TEST PROGRAM")

        print("\nCREATING AND DISPLAYING OF SUBSCRIBERS")

        sub1 = Subscriber('1839456', 'John', 'Doe', 23)
        sub2 = Subscriber('1630236', 'Nicolas', 'Gagnon', 8)
        sub3 = Subscriber('1269348', 'Martin', 'Tremblay', 18)
        print(sub1.info())
        print(sub2.info())
        print(sub3.info())

        print("\nCREATING AND DISPLAYING OF BOOKS")
        book7 = Book("HB514", "Bjh D++", 2010, 9, 3, 4)
        book1 = Book("GA403", "Big C++", 2009, 8, 3, 3)
        book2 = Book("QA203", "Calcul a plusieurs variables partie 1", 2011, 3, 2, 2)
        book3 = Book("QA204", "Calcul a plusieurs variables partie 2", 2011, 3, 2, 2)
        book4 = Book("AC409", "Le chateau d'Ortrante", 1764, 16, 1, 1)
        book5 = Book("BD302", "Harry Potter et le prisonier d'Azkaban", 1999, 3, 1, 1)
        book6 = Book("CE413", "Ibssz Qpuufs et le prisonier c'balbcbo", 2000, 4, 2, 2)
        print(book1.info())
        print(book2.info())
        print(book3.info())
        print(book4.info())
        print(book5.info())
        print(book6.info())
        print(book7.info())

        print("\nBORROWING A BOOK BY A SUBSCRIBER")
        borrow1 = Borrow(sub1, book2, 2020)
        borrow2 = Borrow(sub2, book1, 2020)
        print(borrow1.info())
        print(borrow2.info())

        # / ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
        # / *BEGINNING OF TESTS                                                                                * /
        # / *Remaining modifications are at the end of the main function.                                      * /
        # / ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /

        print("\nADDING OF BOOKS AND SUBSCRIBERS TO THE LIBRARY")
        subscribers = list()  # declaration of an empty list of subscribers
        books = list()  # declaration of an empty list of books
        borrowers = list()  # declaration of an empty list of borrowers
        n_subscribers: int = 0
        n_books: int = 0
        n_borrowers: int = 0

        lib = Library(subscribers, n_subscribers, books, n_books, borrowers, n_borrowers)  # create an instance of Library
        lib.add_subscriber_to_library(sub1)
        lib.add_subscriber_to_library(sub2)
        lib.add_subscriber_to_library(sub3)
        lib.add_subscriber_to_library(sub1)
        lib.add_book_to_library(book1)
        lib.add_book_to_library(book2)
        lib.add_book_to_library(book3)
        lib.add_book_to_library(book4)
        lib.add_book_to_library(book5)
        lib.add_book_to_library(book6)
        lib.add_book_to_library(book7)
        lib.add_book_to_library(book3)
        lib.add_book_to_library(book1)

        print("\nSEARCH BY TITLE...: Calcul")
        title = "Calcul"
        lib.search_book_title(title)

        title = random.choice([book_obj.get_title for book_obj in lib.books])
        print(f"\nSEARCH A RANDOM TITLE ...: {title}")
        # print(title)
        lib.search_book_title(title)

        print("\nSEARCH BY QUOTE...: AC409")

        lib.search_book_quote("AC409")
        lib.search_book_quote("BD302")
        lib.search_book_quote("QA204")
        lib.search_book_quote("QA203")
        lib.search_book_quote("AC209")
        quote = random.choice([book_obj.get_quote for book_obj in lib.books])
        # print(quote)
        print(f"\nSEARCH A RANDOM QUOTE...: {quote}")
        lib.search_book_quote(quote)

        print("\nTESTS OF BORROWING")
        lib.borrow_book_by_subscriber("1630236", "AC409", 2021)
        lib.borrow_book_by_subscriber("1630236", "BD302", 2021)
        lib.borrow_book_by_subscriber('1839456', "GA403", 2021)
        lib.borrow_book_by_subscriber('1839456', "GA403", 2021)
        lib.borrow_book_by_subscriber("1839456", "BD302", 2022)
        lib.borrow_book_by_subscriber("1630236", "QA204", 2024)
        lib.borrow_book_by_subscriber("1630236", "QA203", 2044)
        lib.borrow_book_by_subscriber("1630236", "CE413", 2024)

        print("\nSUBSCRIBER INFORMATION BEFORE RETURNING A BOOK")
        lib.subscriber_info("1630236")

        id_number = random.choice([sub_obj.get_id_number for sub_obj in lib.subscribers])
        print(f"\nRANDOM SUBSCRIBER INFORMATION BEFORE RETURNING A BOOK...: {id_number}")
        lib.subscriber_info(id_number)

        print("\nTEST ON BOOKS RETURN")
        lib.return_book_by_subscriber("1630236", "QA204")
        lib.return_book_by_subscriber("1839456", "QA203")

        print(f"\nTEST ON RANDOM RETURN...: {id_number} - {quote}")
        lib.return_book_by_subscriber(id_number, quote)

        print("\nSUBSCRIBER INFORMATION AFTER RETURNING A BOOK")
        lib.subscriber_info("1630236")

        print(f"\nRANDOM SUBSCRIBER INFORMATION AFTER RETURNING A BOOK...: {id_number}")
        lib.subscriber_info(id_number)

        id_number_non_existent = "102030"
        print(f"\nREMOVING A NON EXISTENT SUBSCRIBER FROM THE LIBRARY:...{id_number_non_existent}")
        lib.remove_subscriber_from_library(id_number_non_existent)

        # print(f"{exception}"):
        print("\nEND OF INTEGRATION TEST!!!\n")
        print(f"\nREMOVING A RANDOM SUBSCRIBER FROM THE LIBRARY:...{id_number}")
        lib.remove_subscriber_from_library(id_number)

    except Exception as exception:
        print(f"{exception}")

    finally:
        stop_time = time.time()
        delta_time = stop_time - start_time
        print(f"{stop_time} - {start_time} = {delta_time}")
        print("If you fail to plan, you are planning to fail! Benjamin Franklin")
        print("""To be a dancing master is a special thing.\nBut to be a faceless man, that is something else entirely""")
        print("PROGRAM ENDED SUCCESSFULLY")


if __name__ == '__main__':
    main()
