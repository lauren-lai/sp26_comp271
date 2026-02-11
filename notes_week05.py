from abc import ABC, abstractmethod
from typing import Any
class DresserADT(ABC):
    """ 
    abstract class that represents the Dresser ADT, a fixed size indexed storage. 
    each drawer can have one item of a given type.
    """

    @abstractmethod
    def __init__(self):
        """
        create a dresser with n drawers
        precondition: n>0, default is 2
        """
        pass

    @abstractmethod
    def num_drawers(self) -> int:
        """
        return the number of drawers
        """

    @abstractmethod
    def is_empty(self, i:int) -> bool:
        """
        return True if drawer i is empty
        preondition: i is a valid index, otherwise raise an exception
        """

    @abstractmethod
    def peek(self, i: int) -> item | None:
        """
        return item if drawer i is not empty, None otherwise
        precondition: i is a valid index, otherwise raise an exception
        """

    @abstractmethod
    def put(self, i: int, item: Any) -> bool:
        """
        add item in drawer i if drawer i is empty and return True
        return False otherwise
        """

    @abstractmethod
    def remove(self, i: int) -> Any | None:
        """
        remove and return item in drawer i, return None otherwise
        """

    