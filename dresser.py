from abc import ABC, abstractmethod
from typing import Any


class DresserADT(ABC):
    """
    Abstract class that represents the Dresser ADT, a fixed size indexed storage. 
    Each drawer can have one item of a given type
    """
    #Constructor
    @abstractmethod
    def __init__(self, n: int = 2): 
        """
        Create a dresser with n drawers. 
        Precondition: n>0, default = 2
        """
        pass
    #Accessor Behavior
    @abstractmethod
    def num_drawers(self) -> int:
        """
        Return the number of drawers.
        """
        pass

    @abstractmethod
    def is_empty(self, i: int) -> bool : 
        """
        return True if drawer i is empty, False otherwise. 
        Precondition: i is a valid index, otherwise raise an exception
        """
        pass
    
    @abstractmethod
    def peek(self, i : int) -> Any | None:
        """
        return item if drawer i is not empty, None otherwise
        Precondition: i is a valid index, otherwise raise an exception
        """
        pass

    #Mutator Behavior
    @abstractmethod
    def put(self, i: int, item : Any) -> bool : 
        """
        add item in drawer i if drawer is empty and return true
        return false otherwise
        Precondition: i is a valid index, otherwise raise an exception
        """
        pass

    @abstractmethod
    def remove(self, i: int) -> Any : 
        """
        Return the item in drawer i (if not empty) and empty drawer 
        Return None otherwise
        Precondition: i is a valid index, otherwise raise an exception
        """
        pass
    
    @abstractmethod
    def clear(self, i: int) -> None : 
        """
        empty drawer i
        Precondition: i is a valid index, otherwise raise an exception
        """
        pass
        
class Clothing(ABC): 
    """
    Abstract base class representing a generic piece of clothing.

    Each clothing item has common attributes such as:
    - size (e.g., S, M, L)
    - color (string description)

    This class defines behavior common to all clothing types,
    but should not be instantiated directly.
    """

    @abstractmethod
    def __init__(self, size: str, color: str):
        """
        Create a Clothing item
        Precondition: needs a size (string) and color (string)
        """
        pass

    @abstractmethod
    def get_size(self) -> str:
        """
        Return the size attribute
        """
        pass

    @abstractmethod
    def get_color(self) -> color:
        """
        Return the color attribute
        """
        pass

class Shirts(Clothing):
    """
    A class that extends the Clothing class to represent shirts, adds the is_short_sleeve attribute
    """
    
    def __init__(self, size: str, color: str, is_short_sleeve: bool):
        self.__size = size
        self.__color = color
        self.__is_short_sleeve = is_short_sleeve

    def get_size(self) -> str:
        return self.__size

    def get_color(self) -> color:
        return self.__color

    def is_short_sleeve() -> bool:
        return self.__is_short_sleeve

class Pants(Clothing):
    """
    A class that extends the Clothing class to represent pants, adds the is_jean attribute
    """
    def __init__(self, size: str, color: str, is_jean: bool):
        self.__size = size
        self.__color = color
        self.__is_jean = is_jean

    def get_size(self) -> str:
        return self.__size

    def get_color(self) -> color:
        return self.__color

    def is_jean() -> bool:
        return self.__is_jean
  
class Dresser(DresserADT): 
    """
    Data Structure extending the DresserADT
    using a python list of length n 
    where all elements imitialized to None (to mean empty)
    where each element is of type: Clothing
    """
    def __init__(self, n: int = 2): 
        """
        Create a dresser with n drawers. 
        Precondition: n>0, default = 2
        """
        self.__dresser = [None] * n
        self.__n = n

    _REPORT_HEADER = 'There are {} entries in your dresser'
    def report(self) -> []: # modified from week03
        """Generate a nicely formatted report of all characters in the show."""
        output = self._REPORT_HEADER.format(len(self.__dresser))
        for i in range(len(self.__dresser)):
            output += f"\n\t{self.__dresser[i]}"
        return output

    def num_drawers(self) -> int:
        """
        Return the number of drawers.
        """
        return self.__n

    def valid_index(self, i: int) -> bool:
        """
        Returns True if i is greater than or equal to 2, and less than or equal to n
        """
        return (2 <= i) and (i <= self.__n)

    def is_empty(self, i: int) -> bool : 
        """
        return True if drawer i is empty, False otherwise. 
        Precondition: i is a valid index, otherwise raise an exception
        """
        to_return = False

        if self.valid_index(i):
            if self.__dresser[i] is None:
                to_return = True
        
        return to_return
    
    def peek(self, i : int) -> Any | None:
        """
        return item if drawer i is not empty, None otherwise
        Precondition: i is a valid index, otherwise raise an exception
        """
        to_return = None
        if self.valid_index(i):
            to_return = self.__dresser[i]
        
        return to_return

    def put(self, i: int, item : Any) -> bool : 
        """
        add item in drawer i if drawer is empty and return true
        return false otherwise
        Precondition: i is a valid index, otherwise raise an exception
        """
        to_return = False
        if self.valid_index(i):
            if (self.__dresser[i] is None):
                self.__dresser[i] = item
                to_return = True
        
        return to_return

    def remove(self, i: int) -> Any:
        """
        Return the item in drawer i (if not empty) and empty drawer 
        Return None otherwise
        Precondition: i is a valid index, otherwise raise an exception
        """
        to_return = None
        if self.valid_index(i):
            if (self.__dresser[i] is not None):
                to_return = self.__dresser[i]
                self.__dresser[i] = None

        return to_return
    
    def clear(self, i: int) -> None: 
        """
        empty drawer i
        Precondition: i is a valid index, otherwise raise an exception
        """
        if self.valid_index(i):
            self.__dresser[i] = None


if __name__ == "__main__": 
    num: int = 10
    my_dresser = Dresser(num)
    print(my_dresser.report())

    my_shirt = Shirts("medium", "blue", True)

    for i in range(num):
        my_dresser.put(i, my_shirt)

    print(my_dresser.report())
