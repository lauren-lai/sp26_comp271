# code for week03 assignment, due feb 6

class Character:
    """A class to represent a character in a show."""

    def __init__(self, first_name: str, last_name: str, role: str):
        """Initialize a Character object with the specified first name,
        last name, and role."""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__role = role

    def __str__(self) -> str:
        """Returns a string representation of the Character object. Specifically,
        the string consists of the first letter of the first name, last name,
        and role concatenated together.
        """
        return (
            ("" if self.__first_name == "" else self.__first_name[0])
            + ("" if self.__last_name == "" else self.__last_name[0])
            + ("" if self.__role == "" else self.__role[0])
        )

    def __repr__(self) -> str:
        """Returns a string representation of the Character object for debugging"""
        return self.__str__()

    def get_first_name(self) -> str:
        """Accessor for the first name of the character."""
        return self.__first_name

    def get_last_name(self) -> str:
        """Accessor for the last name of the character."""
        return self.__last_name

    def get_role(self) -> str:
        """Accessor for the role of the character."""
        return self.__role


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

    def __contains_by(self, target: str, getter) -> bool:
        """Return True if any character's getter() equals target.
        Here's something wonderful about Python: we can pass functions
        as arguments to other functions. In this case, we can pass in
        any of the getter methods defined in the Character class
        (get_first_name, get_last_name, or get_role) and use that
        to compare against the target string. This allows us to
        avoid duplicating code for each of the three "contains" methods.

        This method is private (indicated by the leading double underscore)
        because it is only intended to be used internally by the other
        "contains" methods."""
        # Prepare to iterate through the underlying list
        i = 0
        # Assume we wont find what we are looking for
        found = False
        # Iterate through the list until we either find a match
        # or run out of items to check
        while i < len(self.__underlying) and not found:
            # Check if the current character's getter() matches target
            # Note that we call the getter function passed in as an argument
            # rather than trying to access it as an attribute of the Character
            # object. If we get a match, variable found becomes True and
            # the loop will exit.
            found = getter(self.__underlying[i]) == target
            # Move to the next character in the list
            i += 1
        # Done searching, return whether we found a match
        return found

    def contains_first_name(self, first_name: str) -> bool:
        """Return True if any character has the specified first name.
        This is a public method that uses the private __contains_by()
        method to perform the actual search."""
        return self.__contains_by(first_name, Character.get_first_name)

    def contains_last_name(self, last_name: str) -> bool:
        """Return True if any character has the specified last name.
        This is a public method that uses the private __contains_by()
        method to perform the actual search."""
        return self.__contains_by(last_name, Character.get_last_name)

    def contains_role(self, role: str) -> bool:
        """Return True if any character has the specified role.
        This is a public method that uses the private __contains_by()
        method to perform the actual search."""
        return self.__contains_by(role, Character.get_role)

    # Constant string template for the report header - used in report()
    # In compliance with the "no magic value" principle
    _REPORT_HEADER = 'There are {} characters in your data about "{}"'

    def report(self) -> str:
        """Generate a nicely formatted report of all characters in the show."""
        output = self._REPORT_HEADER.format(len(self.__underlying), self.__title)
        for character in self.__underlying:
            output += f"\n\t{character.get_first_name()} {character.get_last_name()} - {character.get_role()}"
        return output

    def add_unique(self, first_name: str, last_name: str, role: str) -> bool:
        # adds a Character to the Cast object only if there is no other object with the same first name, last 
        # name, and role description. The method returns True if the addition was succesful and False otherwise.
        to_return = False
        if not self.contains_first_name(first_name) or not self.contains_last_name(last_name) or not self.contains_role(role):
            self.add_character(first_name, last_name, role)
            to_return = True
        return to_return
    
    def remove(self, first_name: str, last_name: str, role: str) -> Character | None:
        # removes and returns the first Character object that matches the specified first name and last name and role. 
        # If no such object exists, the method shall return None.
        removed = None
        if self.contains_first_name(first_name) and self.contains_last_name(last_name) and self.contains_role(role):
            i = 0
            index = -1
            while i < len(self.__underlying) and index == -1:
                if self.__underlying[i].get_first_name() == first_name:
                    index = i
                    removed = self.__underlying.pop(index)
                i += 1
        return removed

class Main:
    cast = Cast("Criminal Minds")

    # testing adds
    cast.add_character("aaron", "hotchner", "unit chief")
    cast.add_character("emily", "prentiss", "goat")
    cast.add_character("spencer", "reid", "genius")
    cast.add_character("jennifer", "jareau", "media liason")
    cast.add_unique("haley", "hotchner", "wife") # works because diff first name and role
    print(cast.report())

    # testing remove
    print(cast.remove("aaron", "hotchner", "unit chief"))
    print(cast.remove("emily", "prentiss", "goat"))

    print(cast.report())

    


    