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
        return super().__str__() + f", {role}"

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

    def __str__(self) -> str:
        return f"The title of this show is {self.__title}"

    _REPORT_HEADER = 'There are {} entries in your data about "{}"'
    def report(self) -> []: # modified from week03
        """Generate a nicely formatted report of all characters in the show."""
        output = self._REPORT_HEADER.format(len(self.__underlying), self.__title)
        for i in range(len(self.__underlying)):
            output += f"\n\t{self.__underlying[i]}"
        return output
        
    def add_character(self, first_name: str, last_name: str, role: str) -> None:
        """Add a new character to the show."""
        # First create a new Character object, then append it to the
        # object's underlying list. The following two steps can be
        # done in one step, but for illustration purposes they are
        # shown separately here.
        new_character = Character(first_name, last_name, role)
        self.__underlying.append([None, new_character])

    def add_actor(self, first_name: str, last_name: str) -> None:
        """ Add a new actor to the show """
        # creates and adds an actor to .__underlying, with None for the character
        new_actor = Actor(first_name, last_name)
        self.__underlying.append([new_actor, None])

    __CHARACTER_INDEX: int = 1
    def index_of_character(self, first_name: str, last_name: str, role: str) -> int:
        """Returns the index position of a specified character object. If
        the object is not found, the method returns -1."""
        index: int = -1
        i: int = 0
        while i < len(self.__underlying) and index < 0:
            candidate = self.__underlying[i][self.__CHARACTER_INDEX] # had to add because __underlying is a list of lists
            if candidate != None:
                if (
                    candidate.get_first_name() == first_name
                    and candidate.get_last_name() == last_name
                    and candidate.get_role() == role
                ):
                    index = i
            i = i + 1
        return index
    
    __ACTOR_INDEX: int = 0
    def index_of_actor(self, first_name: str, last_name: str) -> int:
        index: int = -1
        i: int = 0
        while i < len(self.__underlying) and index < 0:
            candidate = self.__underlying[i][self.__ACTOR_INDEX]
            if candidate != None:
                if candidate != None:
                    if (
                        candidate.get_first_name() == first_name
                        and candidate.get_last_name() == last_name
                    ):
                        index = i
            i = i + 1 
        return index

    def add_unique_character(self, first_name: str, last_name: str, role: str) -> bool:
        """Improves class `Cast` by allowing to add a `Character` to the `Cast`
        object only if there is no other object with the same first name,
        last name, and role description. The method returns `True` if the addition
        was succesful and `False` otherwise.
        """
        found: bool = self.index_of_character(first_name, last_name, role) > -1
        if not found:
            self.add_character(first_name, last_name, role)
        return not found
        
    def add_unique_actor(self, first_name: str, last_name: str):
        found: bool = self.index_of_actor(first_name, last_name) > -1
        if not found:
            self.add_actor(first_name, last_name)
        return not found

    def remove_entry(self, index: int):
        self.__underlying.pop(index)
       
    def combine_actor_character(self, actor: Actor, character: Character):
        self.__underlying.append([actor, character])
        
    def assign_to_character(self, character_first_name, character_last_name, 
        character_role, actor_first_name, actor_last_name) -> None:

        # checks if the character and actor already exist in __underlying
        character_index = self.index_of_character(character_first_name, character_last_name, character_role)
        actor_index = self.index_of_actor(actor_first_name, actor_last_name)
        
        # creates Character and Actor objects
        character = Character(character_first_name, character_last_name, character_role)
        actor = Actor(actor_first_name, actor_last_name)

        # if [Actor, None] and [None, Character] -> combine into [Actor, Character]
        if (actor_index != -1) and (character_index != -1):
            self.remove_entry(actor_index)
            self.remove_entry(character_index)
            self.combine_actor_character(actor, character)
        # if just [Actor, None] -> create Character -> combine into [Actor, Character]
        elif (actor_index != -1) and (character_index == -1):
            self.remove_entry(actor_index)
            self.combine_actor_character(actor, character)
        # if just [None, Character] -> create Actor -> combine into [Actor, Character]
        elif (actor_index == -1) and (character_index != -1):
            self.remove_entry(character_index)
            self.combine_actor_character(actor, character)
        # if [None, None] -> create Character and Actor -> combine into [Actor, Character]
        elif (actor_index == -1) and (character_index == -1):
            self.combine_actor_character(actor, character)
        # if [Actor, Character] -> do nothing


if __name__ == "__main__": 

    cast = Cast("The Pitt (2025)")
    print(cast)

    cast.add_character("Michael", "Robinavitch", "Chief of ED")
    cast.add_character("Jack", "Abbot", "Night Shift Attending")
    print(cast.add_unique_character("Michael", "Robinavitch", "Chief of ED")) # prints False
    print(cast.add_unique_character("Victoria", "Javadi", "3rd-Year Med Student")) # prints True
    print(cast.report())

    cast.add_actor("Noah", "Wyle")
    cast.add_actor("Katherine", "LaNasa")
    print(cast.add_unique_actor("Katherine", "LaNasa")) # prints False
    print(cast.add_unique_actor("Patrick", "Ball")) # prints True

    cast.assign_to_character("Michael", "Robinavitch", "Chief of ED", "Noah", "Wyle") # actor and character
    cast.assign_to_character("Dana", "Evans", "Charge Nurse", "Katherine", "LaNasa") # actor no character
    cast.assign_to_character("Jack", "Abbot", "Night Shift Attending", "Shawn", "Hatosy") # no actor and character
    cast.assign_to_character("Trinity", "Santos", "Goat", "Isa", "Briones") # no actor no character

    print(cast.report())