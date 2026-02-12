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
            self.combine_actor_character(actor, character)
            self.remove_entry(actor_index)
            character_index -= 1 # list decreased by 1
            self.remove_entry(character_index)
        # if just [Actor, None] -> create Character -> combine into [Actor, Character]
        elif (actor_index != -1) and (character_index == -1):
            self.combine_actor_character(actor, character)
            self.remove_entry(actor_index)
        # if just [None, Character] -> create Actor -> combine into [Actor, Character]
        elif (actor_index == -1) and (character_index != -1):
            self.combine_actor_character(actor, character)
            self.remove_entry(character_index)
        # if [None, None] -> create Character and Actor -> combine into [Actor, Character]
        elif (actor_index == -1) and (character_index == -1):
            self.combine_actor_character(actor, character)
        # if [Actor, Character] -> do nothing


# if __name__ == "__main__": 
#     cast = Cast("The Pitt (2025)")
#     print(cast)

#     cast.add_character("Michael", "Robinavitch", "Chief of ED")
#     cast.add_character("Jack", "Abbot", "Night Shift Attending")
#     print(cast.add_unique_character("Michael", "Robinavitch", "Chief of ED")) # prints False
#     print(cast.add_unique_character("Victoria", "Javadi", "3rd-Year Med Student")) # prints True

#     cast.add_actor("Noah", "Wyle")
#     cast.add_actor("Katherine", "LaNasa")
#     print(cast.add_unique_actor("Katherine", "LaNasa")) # prints False
#     print(cast.add_unique_actor("Patrick", "Ball")) # prints True

#     print(cast.report())

#     cast.assign_to_character("Michael", "Robinavitch", "Chief of ED", "Noah", "Wyle") # actor and character
#     print(cast.report())
#     cast.assign_to_character("Dana", "Evans", "Charge Nurse", "Katherine", "LaNasa") # actor no character
#     print(cast.report())
#     cast.assign_to_character("Jack", "Abbot", "Night Shift Attending", "Shawn", "Hatosy") # no actor and character
#     print(cast.report())
#     cast.assign_to_character("Trinity", "Santos", "Goat", "Isa", "Briones") # no actor no character

#     print(cast.report())

class TestCast(Cast):
    """Extend Cast to allow access to the underlying list for testing purposes. 
    This is not a good practice in general, but it is done here for 
    testing purposes only."""

    def __init__(self, title: str):
        super().__init__(title)

    def get_underlying(self):
        return self._Cast__underlying


# Testing data for characters
test_data_characters = [
    ("Nyota", "Uhura", "Communications Officer"),
    ("Leonard", "McCoy", "Chief Medical Officer"),
    ("Spock", "", "Science Officer"),
]

# Testing data for actors
test_data_actors = [
    ("Zoe", "Saldana"),
    ("Karl", "Urban"),
    ("Zachary", "Quinto"),
]

# Testing add_character()
test = TestCast("misc")

for f, l, r in test_data_characters:
    test.add_character(f, l, r)

under = test.get_underlying()

test_character_only = True
for u in under:
    a, c = u
    test_character_only = test_character_only and a is None and c is not None
    first_name = c.get_first_name()
    last_name = c.get_last_name()
    role = c.get_role()
    test_character_only = (
        test_character_only and (first_name, last_name, role) in test_data_characters
    )
print("                          add_character() test passed:", test_character_only)

# Testing add_actor()
test = TestCast("misc")

for f, l in test_data_actors:
    test.add_actor(f, l)

under = test.get_underlying()
test_actor_only = True
for u in under:
    a, c = u
    test_actor_only = test_actor_only and a is not None and c is None
    first_name = a.get_first_name()
    last_name = a.get_last_name()
    test_actor_only = test_actor_only and (first_name, last_name) in test_data_actors
print("                              add_actor() test passed:", test_actor_only)

# Prepare to test disjoined add_actor() and add_character() by adding
# characters to be matched to existing actors
for f, l, r in test_data_characters:
    test.add_character(f, l, r)

under = test.get_underlying()
# Simple test to check that the number of entries in the underlying
# list is equal to the sum of the number of characters and actors
# added, which would be the case if add_actor() and add_character()
# are disjoined.
test_disjoined = len(under) == len(test_data_characters) + len(test_data_actors)
print("Disjoined add_actor() and add_character() test passed:", test_disjoined)

# Testing assign_to_character()
test.assign_to_character("Spock", "", "Science Officer", "Zachary", "Quinto")
under = test.get_underlying()
test_assignment = False
for u in under:
    a, c = u
    if (
        a is not None
        and c is not None
        and a.get_first_name() == "Zachary"
        and a.get_last_name() == "Quinto"
        and c.get_first_name() == "Spock"
        and c.get_last_name() == ""
        and c.get_role() == "Science Officer"
    ):
        test_assignment = True
print("                    assign_to_character() test passed:", test_assignment)

# Testing additional disjoined cases by simply verifying that the number of
# entries in the underlying list is equal to the sum of the number of characters
# and actors added, which would be the case if add_actor() and add_character()
#  are disjoined.
test.assign_to_character("Leonard", "McCoy", "Chief Medical Officer", "Karl", "Urban")
test.assign_to_character("Nyota", "Uhura", "Communications Officer", "Zoe", "Saldana")
under = test.get_underlying()
test_full_assignment = len(under) == 3
print("               Full assign_to_character() test passed:", test_full_assignment)

# Testing add_unique_character() and add_unique_actor() by trying to add
# duplicates and verifying that the method returns False and that the
# underlying list is not updated.
under = test.get_underlying()
same_length = len(under) == 3
test_uc = (
    test.add_unique_character("Leonard", "McCoy", "Chief Medical Officer")
    and same_length
)
test_ua = test.add_unique_actor("Karl", "Urban") and same_length
print("                   add_unique_character() test passed:", not test_uc)
print("                       add_unique_actor() test passed:", not test_ua)

# Testing add_unique_character() and add_unique_actor() by trying to add
# new entries and verifying that the method returns True and that the
# underlying list is updated.
test.add_unique_character("Hikaru", "Sulu", "Helmsman")
test.assign_to_character("Hikaru", "Sulu", "Helmsman", "John", "Cho")
under = test.get_underlying()
test_add_unique_and_assign = False
for u in under:
    a, c = u
    if (
        a is not None
        and c is not None
        and a.get_first_name() == "John"
        and a.get_last_name() == "Cho"
        and c.get_first_name() == "Hikaru"
        and c.get_last_name() == "Sulu"
        and c.get_role() == "Helmsman"
    ):
        test_add_unique_and_assign = True
print(
    "         assign_to_character() Actor-only test passed:", test_add_unique_and_assign
)

# Testing add_unique_actor() and assign_to_character() by trying to add a 
# new actor and assign it to an existing character, and verifying that 
# the method returns True and that the underlying list is updated.
test.add_unique_actor("Benedict", "Cumberbatch")
test.assign_to_character("Khan", "Noonien Singh", "Eugenics Villain", "Benedict", "Cumberbatch")
under = test.get_underlying()
test_add_unique_and_assign = False
for u in under:
    a, c = u
    if (
        a is not None
        and c is not None
        and a.get_first_name() == "Benedict"
        and a.get_last_name() == "Cumberbatch"
        and c.get_first_name() == "Khan"
        and c.get_last_name() == "Noonien Singh"
        and c.get_role() == "Eugenics Villain"
    ):
        test_add_unique_and_assign = True
print(
    "     assign_to_character() Character-only test passed:",
    test_add_unique_and_assign,
)

#  Test assign_to_character() by trying to assign two totally new
#  entries and verifying that the underlying list is updated with a new
#  [Actor, Character] pair.
test.assign_to_character("Montgomery", "Scott", "Chief Engineer", "Simon", "Pegg")
under = test.get_underlying()
test_add_unique_and_assign = False
for u in under:
    a, c = u
    if (
        a is not None
        and c is not None
        and a.get_first_name() == "Simon"
        and a.get_last_name() == "Pegg"
        and c.get_first_name() == "Montgomery"
        and c.get_last_name() == "Scott"
        and c.get_role() == "Chief Engineer"
    ):
        test_add_unique_and_assign = True
print(
    "assign_to_character() Actor and Character test passed:",
    test_add_unique_and_assign,
)