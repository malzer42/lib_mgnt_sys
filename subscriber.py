"""Definition of the Subscriber class."""
# Author(s): Pierre Abraham Mulamba
# Date of creation (modification): 20200224 (20200224)
# Usage: import the subscriber
#        create an object sub = Subscriber("102030", "Pierre", "Abraham", 20)

from dataclasses import dataclass


# from borrow import Borrow


@dataclass(init=True, repr=True)
class Subscriber(object):
    """
    Definition of a Subscriber with the following attributes:
    id_number: str
    first_name: str
    last_name: str
    age: int
    borrowers: list[Borrow]
    """
    __slots__ = ['id_number', 'first_name', 'last_name', 'age']
    id_number: str
    first_name: str
    last_name: str
    age: int

    # borrowers: list

    # Accessors methods
    @property
    def get_id_number(self) -> str:
        """
        Access and returns the user id_number
        :return: id_number
        """
        return self.id_number

    @property
    def get_first_name(self) -> str:
        """
        Access and returns the attribute first_name of the class Subscriber
        :return: the attribute first_name
        """
        return self.first_name

    @property
    def get_last_name(self) -> str:
        """
        Accesses and returns the attribute last_name of the class Subscriber
        :return: the attribute last_name
        """
        return self.last_name

    @property
    def get_age(self) -> int:
        """
        Accesses and returns the attribute age of the class Subscriber
        :return: age
        """
        return self.age

    # Mutators methods
    def set_id_number(self, id_number):
        """
        Mutator method to set the attribute id_number of the class Subscriber
        :param id_number:str
        """
        self.id_number = id_number

    def set_first_name(self, first_name):
        """
        Mutator method to set the attribute first_name of the class Subscriber
        :param first_name: str
        :return: void
        """
        self.first_name = first_name

    def set_last_name(self, last_name):
        """
        Mutator method to set the attribute last_name of the class Attribute
        :param last_name: str
        :return: void
        """
        self.last_name = last_name

    def set_age(self, age):
        """
        Set the age
        :param age: int
        :return: void
        """
        self.age = age

    def info(self):
        """
        Method to access and return the attributes of the class Subscriber
        :return: void
        """
        return f"{self.get_first_name}, {self.get_last_name}. {self.get_age} y.o. #{self.get_id_number}"
