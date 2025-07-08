"""Definition of the Book class."""
# Author(s): Pierre Abraham Mulamba
# Date of creation (modification): 20200224 (20200224)
# Usage: import book
#        create an object book = Book('GA403', 'Big C++', 2009, 8, 0, 0)

from dataclasses import dataclass


@dataclass(init=True, repr=True)
class Book(object):
    """
    Definition of a Book with the following attributes:
    quote
    title
    year
    minimal_age
    n_possess
    n_available.
    """
    nBooks = 0
    __slots__ = ['quote', 'title', 'year', 'minimal_age', 'n_possess', 'n_available']
    quote: str
    title: str
    year: int
    minimal_age: int
    n_possess: int
    n_available: int
    nBooks += 1

    # Accessors methods
    @property
    def get_quote(self) -> str:
        """
        Accesses and returns the quote attribute of the class Book
        :return: the attribute quote
        """
        return self.quote

    @property
    def get_title(self) -> str:
        """
        Accesses and returns the title attribute of the class Book
        :return: title
        """
        return self.title

    @property
    def get_year(self) -> int:
        """
        Accesses and returns the year attribute of the class Book
        :return: year
        """
        return self.year

    @property
    def get_minimal_age(self) -> int:
        """
        Accesses and returns the attribute minimal_age of the class Book
        :return: minimal_age
        """
        return self.minimal_age

    @property
    def get_n_possess(self) -> int:
        """
        Accesses and returns the attribute n_possess of the class Book
        :return: n_possess
        """
        return self.n_possess

    @property
    def get_n_available(self) -> int:
        """
        Accesses and returns the attribute n_available of the class Book
        :return: n_available
        """
        return self.n_available

    # Mutators methods
    def set_quote(self, quote:str):
        """
        Mutator method to set the attribute quote of the class Book
        :param quote: str
        :return: void
        """
        self.quote = quote

    def set_title(self, title:str):
        """
        Mutator method to set the attribute title of the class Book
        :param title: str
        :return: void
        """
        self.title = title

    def set_year(self, year:int):
        """
        Mutator method to set the attribute year of the class Book
        :param year: int
        :return: void
        """
        self.year = year

    def set_minimal_age(self, minimal_age:int):
        """
        Mutator method to set the attribute minimal_age of the class Book
        :param minimal_age: int
        :return: void
        """
        self.minimal_age = minimal_age

    def set_n_possess(self, n_possess:int):
        """
        Mutator method to set the attribute n_possess of the class Book
        :param n_possess:
        :return: void
        """
        self.n_possess = n_possess

    def set_n_available(self, n_available:int):
        """
        Mutator method to set the attribute n_available of the class Book
        :param n_available: int
        :return: void
        """
        self.n_available = n_available

    def info(self):
        """
        Method to access and return the attributes of the class Book
        :return: void:
        """
        return f"{self.get_quote}. {self.get_title}. {self.get_minimal_age} y.o."
