"""Definition of the Borrow class."""
# Author(s): Pierre Abraham Mulamba
# Date of creation (modification): 20200224 (20200224)
# Usage: import the borrow
#        create an object borrow = Borrow("102030", "Pierre", "Abraham", 20)

from dataclasses import dataclass
from subscriber import Subscriber
from book import Book


@dataclass(init=True, repr=True)
class Borrow(object):
    """
    Definition of a Borrow with the following attributes:
    sub_obj
    book_obj
    date_obj.
    """
    __slots__ = ['sub_obj', 'book_obj', 'book_return_date']
    sub_obj: Subscriber
    book_obj: Book
    book_return_date: int

    @property
    def get_sub_obj(self) -> Subscriber:
        """
        Returns the attribute sub_obj of the class Borrow
        :return: sub_obj: Subscriber
        """
        return self.sub_obj

    @property
    def get_book_obj(self) -> Book:
        """
        Returns the attribute book_obj of the class Borrow
        :return: book_obj: Book
        """
        return self.book_obj

    @property
    def get_book_return_date(self) -> int:
        """
        Returns the attribute book_return_date of the class Borrow
        :return: book_return_date: int
        """
        return self.book_return_date

    # Mutators methods
    def set_sub_obj(self, sub_obj: Subscriber):
        """
        Setting the attribute sub_obj
        :param sub_obj: Subscriber
        :return: void
        """
        self.sub_obj = sub_obj

    def set_book_obj(self, book_obj : Book):
        """
        Mutator method to set the attribute book_obj of the class Borrow
        :param book_obj: Book
        :return:  void
        """
        self.book_obj = book_obj

    def set_book_return_date(self, book_return_date:int):
        """
        Mutator method to set the attribute the book_return_date
        :param book_return_date: int
        :return: void
        """
        self.book_return_date = book_return_date

    def info(self):
        """
        Method to access and return the attributes of the class Borrow
        :return: void
        """
        try:
            return f"{self.book_obj.get_quote} borrowed by {self.sub_obj.get_id_number}"
        except Exception as exception_info:
            print(exception_info)
        finally:
            pass
