"""Definition of the Library class."""
# Author(s): Pierre Abraham Mulamba
# Date of creation (modification): 20200224 (20200224)
# Usage: import book
#        create an object book = Book('GA403', 'Big C++', 2009, 8, 0, 0)
# tmp_subscriber = Subscriber('', '', '', 0)

# for subscriber in self.subscribers:
#    if subscriber.get_id_number == id_number:
#        tmp_subscriber = subscriber
#        break
# self.subscribers.remove(tmp_subscriber)
# del tmp_subscriber
# tmp_book = Book('', '', 2020, 0, 0, 0)
# for book in self.books:
#    if book.get_quote == quote_book:
#        tmp_book = book
#        break
# self.books.remove(tmp_book)
# del tmp_book
# for book in self.books:
#    if title in book.get_title:
#        print(book.info())
# for book in self.books:
#    if quote_to_search in book.get_quote:
#        print(book.info())

from dataclasses import dataclass
from typing import List

from book import Book
from borrow import Borrow
from subscriber import Subscriber


@dataclass(init=True, repr=True)
class Library(object):
    """
    Definition to the Library class with the following attributes:
    subscribers: List[Subscriber]
    n_subscribers: int
    books: List[Book]
    n_books: int
    borrowers: List[Borrow]
    n_borrowers: int
    """
    __slots__ = ['subscribers', 'n_subscribers', 'books', 'n_books', 'borrowers', 'n_borrowers']

    subscribers: List[Subscriber]
    n_subscribers: int
    books: List[Book]
    n_books: int
    borrowers: List[Borrow]
    n_borrowers: int

    def add_subscriber_to_library(self, subscriber_obj: Subscriber):
        """
        Adding a Subscriber object to the library
        subscriber_obj: Subscriber instance.
        """
        try:
            if subscriber_obj not in self.subscribers:
                self.subscribers.append(subscriber_obj)
                self.n_subscribers = len(self.subscribers)
                print(f"{subscriber_obj.get_id_number} added successfully")
            else:
                print(f"WARNING {subscriber_obj.get_id_number} already exists in the Library")
        except Exception as exception_add_sub:
            print(exception_add_sub)
            raise
        else:
            print(f"Total {len(self.subscribers)} subscriber(s) added to the Library")
        finally:
            print("Done")

    def remove_subscriber_from_library(self, id_number:str):
        """
        Remove a Subscriber based on his id_number
        id_number: str
        """
        try:
            [self.subscribers.remove(sub_obj) for sub_obj in self.subscribers if sub_obj.get_id_number == id_number][0]
            print(f"{id_number} removed successfully")
            self.n_subscribers = len(self.subscribers)
        except IndexError as index_error:
            print(f"{id_number} Non existent in the Library - {index_error}")
        except Exception as exception_rem_sub:
            print(f"{id_number} Non  existent in the Library - {exception_rem_sub}")
            raise
        else:
            print(f"Total {len(self.subscribers)} subscriber(s) in the Library")

        finally:
            print("Done")

    def add_book_to_library(self, book_obj:Book):
        """
        Adding a Book instance to the library
        book_obj: Book instance.
        """
        try:
            if book_obj not in self.books:
                self.books.append(book_obj)
                self.n_books = len(self.books)
                print(f"{book_obj.get_quote} added successfully")
            else:
                print(f"WARNING {book_obj.get_quote} already exists in the Library")
        except Exception as exception_add_book:
            print(exception_add_book)
            raise
        else:
            print(f"Total of {len(self.books)} book(s) added to the Library")
        finally:
            print("Done")

    def remove_book_from_library(self, quote_book:str):
        """
        Remove a book from the library based on the quote of the book
        quote_book: str
        """
        try:
            [self.books.remove(book_obj) for book_obj in self.books if book_obj.get_quote == quote_book][0]
            self.n_books = len(self.books)
            print(f"{quote_book} removed successfully")
        except Exception as exception_rem_book:
            print(f"{quote_book} is not in the Library - {exception_rem_book}")
            raise
        else:
            print(f"Total {len(self.books)} book(s) in the Library")
        finally:
            print("Done")

    def search_book_title(self, title):
        """
        Search and display all the book with the title containing the text_to_find
        title: str
        """
        try:
            [print(book_obj.info()) for book_obj in self.books if title in book_obj.get_title]
        except Exception as exception_search_title:
            print(f"{title} Not found - {exception_search_title}")
            raise
        else:
            print(f"Title {title} found!")
        finally:
            pass

    def search_book_quote(self, quote_to_search):
        """
        Search and display information about a book based on the quote of the book
        quote_to_search: str
        """
        try:
            for book_obj in self.books:
                if quote_to_search in book_obj.get_quote:
                    print(f"{book_obj.info()} found!")
                    return
        except Exception as exception_quote:
            print(f"{quote_to_search} -- {exception_quote}")
            raise
        else:
            pass
        finally:
            pass

    def borrow_book_by_subscriber(self, sub_id_number, book_quote, book_return_date) -> bool:
        """
        The method check if it is possible that the book can be borrowed by the subscriber
        if it is possible, then a new borrow is added to the list of borrowers.
        It is possible to borrow a book by a subscriber if the book is available,
        the subscriber as the minimal required age to read the book,
        the subscriber did not already borrow the book
        the subscriber did not exceed the maximal number (2) of books to borrow.
        :param sub_id_number: str
        :param book_quote: str
        :param book_return_date: date
        :return: bool, True in case of success borrow and False otherwise
        """
        success_or_fail: bool = False
        number_of_books_borrowed_by_subscriber: int = 0
        maximal_number_to_borrow: int = 2

        try:
            # Search a book with the given book_quote in the list of books and assign it to tmp_book
            # Check if the book is available in the list of books.
            book_obj = [book_elt for book_elt in self.books if book_elt.get_quote == book_quote][0]

            if book_obj.get_n_available > 0:
                is_book_available = True
            else:
                print(f"{book_obj.get_quote} is not available {book_obj.get_n_available}")
                return success_or_fail

            sub_obj = [subscriber_elt for subscriber_elt in self.subscribers if subscriber_elt.get_id_number == sub_id_number][0]

            # Check if the given subscriber has borrowed the book in the list of borrowers
            # Count the number of time the subscriber occurs in the borrowers list
            has_subscriber_borrowed_the_book: bool = False
            borrow_obj = Borrow(sub_obj, book_obj, book_return_date)
            if borrow_obj in self.borrowers:
                print(f"{borrow_obj.get_book_obj.get_quote} - {borrow_obj.get_sub_obj.get_id_number} exists in the borrowers list")
                return success_or_fail

            for borrow_elt in self.borrowers:
                if borrow_elt.get_sub_obj.get_id_number == sub_id_number:
                    number_of_books_borrowed_by_subscriber = number_of_books_borrowed_by_subscriber + 1
                    if number_of_books_borrowed_by_subscriber >= maximal_number_to_borrow:
                        success_or_fail = False
                        print(f"Number of books borrowed by subscriber {number_of_books_borrowed_by_subscriber}")
                        print(f"{sub_obj.get_id_number} has reached the limit to borrow a book")
                        # print("Excess Failure to borrow the book {} by the subscriber {}".format(book_obj, sub_obj))
                        return success_or_fail

                    else:
                        print(f"!!!! {number_of_books_borrowed_by_subscriber}. {borrow_elt.get_book_obj.get_quote} - {borrow_elt.get_sub_obj.get_id_number} !!!!")

            # Check if the subscriber has the required age to read the book,
            # the subscriber did not exceed the maximal number allowed to borrow.
            has_required_age: bool = False
            if sub_obj.get_age >= book_obj.get_minimal_age:
                has_required_age = True
            else:
                print(f"{sub_obj.get_id_number} does not have the required age to read the book {book_obj.get_quote}")
                return success_or_fail

            # number_of_books_borrowed_by_subscriber = self.borrowers.count(borrow_obj)

            if number_of_books_borrowed_by_subscriber > maximal_number_to_borrow:
                print(f"{sub_obj.get_id_number} has exceed the limit to borrow a book")
                return success_or_fail

            if has_required_age and is_book_available and number_of_books_borrowed_by_subscriber < maximal_number_to_borrow and not has_subscriber_borrowed_the_book:
                if borrow_obj not in self.borrowers:
                    self.borrowers.append(borrow_obj)
                    book_obj.set_n_available(book_obj.get_n_available - 1)
                    number_of_books_borrowed_by_subscriber += 1
                    print(f"{book_quote} borrowed by {sub_id_number}")
                    success_or_fail = True
                    return success_or_fail
                else:
                    print(f"Number of books borrowed by subscriber {number_of_books_borrowed_by_subscriber}")
                    print(f"Failure to borrow the book {book_obj.get_quote} by the subscriber {sub_obj.get_id_number}")
                    return success_or_fail

        except Exception as exception__borrow_book:
            print(f"{book_obj.get_quote} is not in the library -{exception__borrow_book}")
            raise
        else:
            print(f"Total {len(self.borrowers)} borrow(s) from the Library")
        finally:
            print("Done")
            return success_or_fail

    def return_book_by_subscriber(self, sub_id_number, book_quote) -> bool:
        """
        If a subscriber has borrowed a book, the borrow is removed from the borrowers list
        otherwise nothing is done
        :param sub_id_number: str
        :param book_quote: str
        :return: True/False: bool
        """

        is_book_returned_by_subscriber: bool = False

        try:
            sub_obj = [sub_elt for sub_elt in self.subscribers if sub_elt.get_id_number == sub_id_number][0]
            book_obj = [book_elt for book_elt in self.books if book_elt.get_quote == book_quote][0]
            borrow_obj = [borrow_elt for borrow_elt in self.borrowers if borrow_elt.get_sub_obj == sub_obj and borrow_elt.get_book_obj == book_obj][0]
            if borrow_obj in self.borrowers:
                self.borrowers.remove(borrow_obj)
                is_book_returned_by_subscriber = True
                book_obj.set_n_available(book_obj.get_n_available + 1)
                print(f"Success return of {book_obj.get_quote} by {sub_obj.get_id_number}")
                return is_book_returned_by_subscriber

        except Exception as exception_return_book:
            print(f"Failed return of {book_quote} by {sub_id_number} - {exception_return_book}")
            raise
        else:
            print(f"Total {len(self.borrowers)} borrow(s) in the borrowers list")
        finally:
            print("Done")
            return is_book_returned_by_subscriber

    def subscriber_info(self, sub_id_number):
        """
        Print the subscriber last name, first name and borrowed books
        :param sub_id_number: str
        :return:
        """
        try:
            sub_obj = [sub_elt for sub_elt in self.subscribers if sub_elt.get_id_number == sub_id_number][0]
            print(f"{sub_obj.info()}")
            [print(borrow_obj.info()) for borrow_obj in self.borrowers if borrow_obj.get_sub_obj.get_id_number == sub_id_number]
        except Exception as exception_sub_info:
            print(f"{sub_id_number} Not found in the Library - {exception_sub_info}")
            raise
        else:
            pass
        finally:
            print("Done")
