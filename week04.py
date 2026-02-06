class Person:
    """A super class that lends characteristics to Actors and Characters"""

    def __init__(self, first_name: str, last_name: str):
        """Instantiate a Person object with the given first and last names."""
        self.__first_name = first_name
        self.__last_name = last_name

    # Plain accessors
    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    # String representation and its constants
    __FNU = "First Name Unknown"
    __LNU = "Last Name Unknown"

    def __str__(self) -> str:
        """A string representation suitable for user-facing printing"""
        first = self.__FNU if self.__first_name == "" else self.__first_name
        last = self.__LNU if self.__last_name == "" else self.__last_name
        return f"{first} {last}"

    def __repr__(self) -> str:
        """A string representation suitable for developer-facing printing."""
        return f"{self.__class__.__name__}: {self}"


class Actor(Person):
    """Actor objects are just plain Persons -- the pass statement below
    signals that we don't need anything more than what the superclass Person
    already provides
    """

    pass


class Character(Person):
    """Character objects extend the superclass Person by adding one more
    attribute: a description of the character's role.
    """

    def __init__(self, first_name: str, last_name: str, role: str):
        # First instantiate a Person object by invoking the __init__
        # method of the superclass (Person)
        super().__init__(first_name, last_name)
        # Τhen initialize the role field for the δerived object (Character)
        self.__role = role

    # Plain accessor for the additional field
    def get_role(self) -> str:
        return self.__role

    # Constant for local __str__
    __ROLE_UNKNOWN = "Role Unknown"

    def __str__(self) -> str:
        """Local implementation of the string method to include
        the Character's role in the output. The method uses the
        string function of the superclass object and concatenates
        a string with the role information."""
        role = self.__ROLE_UNKNOWN if self.__role == "" else self.__role
        return super().__str__() + f" {role}"


class Cast:
    """A class to represent the cast of a show, consisting of multiple
    Character objects."""

    def __init__(self, title: str):
        # The title of the show being represented
        self.__title = title
        # A list of Character objects
        self.__underlying = []

    def __len__(self) -> int:
        """Return the number of characters in the show. This allows
        the use of len() on Cast objects."""
        return len(self.__underlying)

    def __bool__(self) -> bool:
        """Return True if there is at least one character in the
        show, False otherwise. This allows the use of bool() on
        Cast objects."""
        return len(self.__underlying) > 0

    def add_character(self, first_name: str, last_name: str, role: str) -> None:
        """Add a new character to the show."""
        # First create a new Character object, then append it to the
        # object's underlying list. The following two steps can be
        # done in one step, but for illustration purposes they are
        # shown separately here.
        new_character = Character(first_name, last_name, role)
        self.__underlying.append(new_character)

    def index_of(self, first_name: str, last_name: str, role: str) -> int:
        """Returns the index position of a specified character object. If
        the object is not found, the method returns -1."""
        # Assume the object is not in the underlying list
        index: int = -1
        # Prepare to traverse the list
        i: int = 0
        # Loop ends as soon as we find a match, by updating variable
        # index to the position of the match, or when we search the
        # entire list with no luck.
        while i < len(self.__underlying) and index < 0:
            # Instead of having three references to the underlying list
            # in the if statement below, let's assign the current item
            # from the list to a local variable.
            candidate = self.__underlying[i]
            if (
                candidate.get_first_name() == first_name
                and candidate.get_last_name() == last_name
                and candidate.get_role() == role
            ):
                # Match found at position i in the underlying list.
                # Save this position to the return variable. This will
                # cause the loop to end.
                index = i
            # Prepare to consider the next elemetn in the underlying list
            i = i + 1
        # Done
        return index

    def add_unique(self, first_name: str, last_name: str, role: str) -> bool:
        """Improves class `Cast` by allowing to add a `Character` to the `Cast`
        object only if there is no other object with the same first name,
        last name, and role description. The method returns `True` if the addition
        was succesful and `False` otherwise.
        """
        found: bool = self.index_of(first_name, last_name, role) > -1
        unique = not found  # superfluous but helps with readability
        if unique:
            # No record found, so we can add it here.
            self.add_character(first_name, last_name, role)
        return unique