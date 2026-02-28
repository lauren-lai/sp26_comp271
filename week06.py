from __future__ import annotations  # Authorized import for advanced type hints
from abc import ABC, abstractmethod  # Authorized import for derived classes

# 345678901234567890123456789012345678901234567890123456789012345678901234567890

# =================================== PART A ===================================

class Node:
    """A simple linkable object. The node comprises two fields: a value field,
    here typed a string, and a pointer field to the next node. The default is
    to instantiate a node with just a value, and no other node to point to it,
    for example:

    +------+
    | node |-next--> None
    +------+

    Nodes are connected to each other later, for example,

    chi = Node("Chicago")        spi = Node("Springfield")
    +------+                     +------+
    | node |-next--> None        | node |-next--> None
    +------+                     +------+

    and then chi.set_next(spi) will result to the arrangement below which is,
    essentially, a linked list.

    chi -----------------------> spi

    +------+                     +------+
    | node |-next--------------> | node |-next--> None
    +------+                     +------+

    """

    def __init__(self, value: str) -> None:
        """Object constructor. Requires only a value to instantiate the object.
        The next object may be assigned later"""
        self.__value: str = value
        self.__next: Node | None = None

    def __str__(self) -> str:
        """Simple string representation of the object."""
        return f"{self.__value}"

    def has_next(self) -> bool:
        """Predicate accessor; tells if object points to
        another object"""
        return self.__next is not None

    def get_next(self) -> Node | None:
        """Standard accessor for next object"""
        return self.__next

    def set_next(self, next: Node) -> None:
        """Mutates object by assigning its next pointer to another object"""
        self.__next = next

    def get_value(self) -> str:
        """Accessor for the object's value"""
        return self.__value


class LinkedList:
    """A simple linked list of Node objects. Nodes in this list are
    connected one after the other, as shown below

      head
    +------+         +------+         +------+        +------+
    | node |-next--> | node |-next--> | node |--> ... | node |-next-->  None
    +------+         +------+         +------+        +------+

    Every node, in the linked list, is connected to another node. Except for
    the last node that points to None.

    Problem 1:
        Instead of walking from head to end, the LinkedList class has a __tail 
        attribute (initialized as None) that keeps track of the last node in the 
        list. When adding a node to the end, add() makes new_node the head and 
        tail (if the list is empty), or sets new_node as the node after __tail,
        and then updates __tail to equal new_node.

    Problem 2:
        In the same way LinkedList contains the __head attribute, adding a 
        __count attribute removes the need for count() to walk from head to end
        every time. __count is incremented by 1 everytime add() is called, and 
        initalizes at 0 because the linked list is initialized empty.
    """

    def __init__(self) -> None:
        """Instantiate an empty linked list"""
        self.__head: Node | None = None
        self.__tail = None
        self.__count = 0

    # Constants for string representation of the linked list
    __EMPTY_LIST_STR: str = "Empty List"
    __RIGHT_ARROW: str = " → "

    def __str__(self) -> str:
        """String representation."""
        # Assume an empty list
        string: str = self.__EMPTY_LIST_STR
        if self.__head is not None:
            # If the list is not empty, we start with the head node and
            # we keep adding the value of the next node, until we reach
            # the end of the list.
            string = self.__head.get_value()
            # Start with the first node and keep adding the next node
            # until we reach the end of the list.
            current: Node = self.__head.get_next()
            while current is not None:
                # Add the next node to the string and move to the next
                # node. The loop ends when we reach the end of the list
                # and current is None.
                string += self.__RIGHT_ARROW + current.get_value()
                current = current.get_next()
        return string

    def add(self, value: str) -> None:
        """
        adds a new node to the linked list. first creates the new node with
        the given value, then adds it to the tail of the list.
        """
        new_node: Node = Node(value)
        # for a list of length 1, head and tail are the same item
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
            self.__count += 1
        # otherwise, set the node after the tail to new_node and update tail
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node
            self.__count += 1

    def count(self) -> int:
        """returns the __count attribute"""
        return self.__count

    def insert(self, new_value: str, after_value: str) -> bool:
        inserted = False
        current = self.__head
        new_node = Node(new_value)

        while (current is not None) and (inserted == False):
            if current.get_value() == after_value:
                if ((after_value == self.__tail.get_value()) 
                and (current.get_next() is None)):
                    self.__tail.set_next(new_node)
                    self.__tail = new_node
                else:
                    prev_next = current.get_next()
                    new_node.set_next(prev_next)
                    current.set_next(new_node)

                self.__count += 1
                inserted = True
            else:
                current = current.get_next()
        return inserted


# =================================== PART B ===================================

class Performance(ABC):
    """
    A general live performance event.

    This class captures the shared structure and behavior of all
    live performances: concerts, lectures, theater productions,
    magic shows, etc.

    The purpose of this class is to define:

        • Common data that every performance has.
        • Common behavior shared by all performances.
        • A contract (via abstract methods) that subclasses must fulfill.

    Subclasses are responsible for defining how revenue is calculated
    and how the performance is described.
    """

    def __init__(
        self, title: str, duration_minutes: int, base_ticket_price: float
    ) -> None:
        """
        Initialize a new performance.

        Parameters:
            title               The name of the event.
            duration_minutes    How long the event lasts.
            base_ticket_price   The standard ticket price before
                                any subclass-specific adjustments.

        Note:
            We use protected attributes (_name style) instead of
            private (__name) because subclasses will need direct
            access to these values.
        """
        self._title: str = title
        self._duration_minutes: int = duration_minutes
        self._base_ticket_price: float = base_ticket_price

        # Number of audience members currently admitted.
        # Starts at zero and increases via admit_audience().
        self._audience_count: int = 0

    # ---------------------------------------------------------
    # Concrete (Fully Implemented) Methods
    # These are inherited as-is by subclasses.
    # ---------------------------------------------------------

    def __str__(self) -> str:
        """
        General string representation.

        We call describe() here so that when a Performance
        object is printed, the subclass version of describe()
        is used automatically (polymorphism in action).
        """
        return self.describe()

    def admit_audience(self, number: int) -> None:
        """
        Adds audience members to the performance.

        Only positive numbers are accepted.
        """
        if number > 0:
            self._audience_count += number

    def get_title(self) -> str:
        """Returns the performance title."""
        return self._title

    def get_duration(self) -> int:
        """Returns the duration in minutes."""
        return self._duration_minutes

    def get_audience_count(self) -> int:
        """Returns the number of admitted audience members."""
        return self._audience_count

    def get_base_ticket_price(self) -> float:
        """
        Returns the base ticket price.

        Subclasses may use this value as the starting point
        for their own pricing logic.
        """
        return self._base_ticket_price

    # ---------------------------------------------------------
    # Abstract Methods (Must Be Implemented by Subclasses)
    # ---------------------------------------------------------

    @abstractmethod
    def calculate_revenue(self) -> float:
        """
        Compute total revenue for the performance.

        Subclasses decide how ticket price is adjusted
        (VIP upgrades, student discounts, special pricing, etc.).

        The result should reflect:
            audience_count × adjusted_ticket_price
        """
        ...

    @abstractmethod
    def describe(self) -> str:
        """
        Return a human-readable description of the performance.

        Each subclass should include details specific
        to its type of event.
        """
        ...


class Concert(Performance):
    """
    Implements Performance to represent a music concert
    """

    def __init__(
        self, title: str, duration_minutes: int, base_ticket_price: float, 
        artist_name: str, genre: str, has_vip: bool
    ) -> None:

        super().__init__(title, duration_minutes, base_ticket_price)
    
        self.__artist_name: str = artist_name
        self.__genre: str = genre
        self.__has_vip: bool = has_vip

    def __str__(self) -> str:
        """
        General string representation.

        We call describe() here so that when a Performance
        object is printed, the subclass version of describe()
        is used automatically (polymorphism in action).
        """
        return self.describe()

    def admit_audience(self, number: int) -> None:
        """
        Adds audience members to the performance.

        Only positive numbers are accepted.
        """
        if number > 0:
            self._audience_count += number

    def get_title(self) -> str:
        """Returns the performance title."""
        return self._title

    def get_duration(self) -> int:
        """Returns the duration in minutes."""
        return self._duration_minutes

    def get_audience_count(self) -> int:
        """Returns the number of admitted audience members."""
        return self._audience_count

    def get_artist_name(self) -> str:
        """returns the artist's name"""
        return self.__artist_name

    def get_genre(self) -> str:
        """returns the genre"""
        return self.__genre
    
    def has_vip(self) -> bool:
        """returns True if there is a vip, False otherwise"""
        return self.__has_vip

    def get_base_ticket_price(self) -> float:
        """
        Returns the base ticket price.

        Subclasses may use this value as the starting point
        for their own pricing logic.
        """
        return self._base_ticket_price

    def get_adjusted_ticket_price(self) -> float:
        """
        returns an increased ticket price if the concert has a vip, otherwise 
        returns the base ticket price.
        """
        adjusted_ticket_price = self.get_base_ticket_price()
        if self.has_vip():
            adjusted_ticket_price = ((self.get_base_ticket_price() * 0.4)
                                    + self.get_base_ticket_price())
        return adjusted_ticket_price

    def calculate_revenue(self) -> float:
        """returns the calculated revenue, attendance x adjusted price."""
        return self.get_audience_count() * self.get_adjusted_ticket_price()
    
    _DESCRIBE_HEADER = "This concert features {}, an artist in {} genre."
    def describe(self) -> str:
        """
        returns a string description of the concert, including the artist's 
        name and genre.
        """
        return self._DESCRIBE_HEADER.format(self.get_artist_name(), 
                                            self.get_genre())

class Lecture(Performance):
    """
    Implements Performance to represent a university Lecture
    """

    def __init__(
        self, title: str, duration_minutes: int, base_ticket_price: float, 
        speaker_name: str, is_university_event: bool
    ) -> None:

        super().__init__(title, duration_minutes, base_ticket_price)

        self.__speaker_name = speaker_name
        self.__is_university_event = is_university_event


    def __str__(self) -> str:
        """
        General string representation.

        We call describe() here so that when a Performance
        object is printed, the subclass version of describe()
        is used automatically (polymorphism in action).
        """
        return self.describe()

    def admit_audience(self, number: int) -> None:
        """
        Adds audience members to the performance.

        Only positive numbers are accepted.
        """
        if number > 0:
            self._audience_count += number

    def get_title(self) -> str:
        """Returns the performance title."""
        return self._title

    def get_duration(self) -> int:
        """Returns the duration in minutes."""
        return self._duration_minutes

    def get_speaker(self) -> str:
        """returns the speaker's name."""
        return self.__speaker_name

    def get_audience_count(self) -> int:
        """Returns the number of admitted audience members."""
        return self._audience_count

    def is_university_event(self) -> bool:
        """returns if this is a university event."""
        return self.__is_university_event

    def get_base_ticket_price(self) -> float:
        """
        Returns the base ticket price.

        Subclasses may use this value as the starting point
        for their own pricing logic.
        """
        return self._base_ticket_price

    def get_adjusted_ticket_price(self) -> float:
        """
        returns a discounted the ticket price if this is a university event, 
        returns the base price otherwise.
        """
        adjusted_ticket_price = self.get_base_ticket_price()
        if self.is_university_event():
            adjusted_ticket_price = adjusted_ticket_price * 0.5
        return adjusted_ticket_price

    def calculate_revenue(self) -> float:
        """returns the calculated revenue, attendance x adjusted price."""
        return self.get_audience_count() * self.get_adjusted_ticket_price()

    _DESCRIBE_HEADER = "This event features {}, and {} a university event."
    def describe(self) -> str:
        """
        Return a human-readable description of the performance.

        Each subclass should include details specific
        to its type of event.
        """
        word = "is" if self.is_university_event() else "is not"
        return self._DESCRIBE_HEADER.format(self.get_speaker(), word)



def main() -> None:

    events: list[Performance] = [
        Concert("Summer Blast", 120, 50.0, "The Meteors", "Rock", True),
        Lecture("AI and Society", 90, 30.0, "Dr. Kwan", True)
    ]   
    events[0].admit_audience(100)
    events[1].admit_audience(100)

    for event in events:
        print(event.describe())
        print(f"The revenue from this event is {event.calculate_revenue()}\n")

    total_revenue = events[0].calculate_revenue() + events[1].calculate_revenue()
    print(f"The total revenue is {total_revenue}")

if __name__ == "__main__":
    main()