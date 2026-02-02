class Character:
    """A character with a unique (first_name, last_name) identity.
    Roles are stored as a list so one character can have multiple roles.
    """

    def __init__(self, first_name, last_name, role):
        self._first_name = first_name
        self._last_name = last_name
        self._roles = [role]

    def __str__(self):
        """Nice string representation for printing."""
        full_name = f"{self.first_name} {self.last_name}".strip()
        roles_str = ", ".join(self.roles)
        return f"{full_name}: {roles_str}"

    # THIS TYPE OF GET/SET IS PYTHON-SPECIFIC
    @property
    def first_name(self):
        """get the first_name"""
        return self._first_name
    
    @first_name.setter
    def first_name(self, new_name):
        """set first_name"""
        if not Character.is_valid_first_name(new_name):
            raise valueError("first_name must not be empty")
        self._first_name = new_name

    @property
    def last_name(self):
        """get last_name"""
        return self._last_name
    
    @last_name.setter
    def last_name(self, new_name):
        """set last_name"""
        if not Character.is_valid_last_name(new_name):
            raise valueError("first_name must not be empty")
        self._last_name = new_name

    def add_role(self, role) -> None:
        """Add a new role if it is not already present."""
        if role is None:
            raise ValueError("role must not be None")
        if role == "":
            raise ValueError("role must not be empty")
        
        if not self.has_role(role):
            self.roles.append(role)

    def has_role(self, role: str) -> bool:
        """check if the provided role belongs to the character"""
        i = 0
        is_role = False
        while i < len(self.roles) and not is_role:
            if self._role[i] == role:
                is_role = True
            i += 1
        return is_role

    def key(self) -> tuple[str, str]:
        """Return a tuple that uniquely identifies this character."""
        result = (self.first_name, self.last_name)
        return result

    def first_name_startswith(self, prefix: str) -> bool:
        """return true if the first name starts with prefix"""
        matches = False
        if prefix is None:
            matches = False
        else:
            matches = self.first_name.startswith(prefix)
        return matches

    def first_name_endswith(self, suffix: str) -> bool:
        """return True if the first name ends with suffix"""
        matches = False
        if suffix is None:
            matches = False
        else:
            matches = self.first_name.endswith(suffix)
        return matches

    @staticmethod
    def is_valid_first_name(name: str) -> bool:
        """return true if the provided name is considered valid first name"""
        valid = True
        if name is None or name == "":
            valid = False
        return valid
    
    @staticmethod
    def is_valid_last_name(name: str) -> bool:
        """return true if the provided name is considered valid last name"""
        valid = True
        if name is None:
            valid = False
        return valid


class Cast:
    """A collection of unique Character records.

    Uniqueness rule: (first_name, last_name) must be unique.
    If the character exists, we add the role to that character.
    """

    def __init__(self) -> None:
        self.__underlying = []  # list[Character]

    def _find_index(self, first_name: str, last_name: str) -> int:
        """Return the index of the character, or -1 if not found."""
        target_key = (first_name, last_name)
        index = -1
        i = 0
        while i < len(self.__underlying) and index == -1:
            if self.__underlying[i].key() == target_key:
                index = i
            i += 1
        return index

    def add_character(self, first_name: str, last_name: str, role: str) -> None:
        """Add a character if new; otherwise attach role to existing character."""
        index = self._find_index(first_name, last_name)
        if index == -1:
            self.__underlying.append(Character(first_name, last_name, role))
        else:
            self.__underlying[index].add_role(role)

    def indices_prefix(self, prefix: str) -> list[int]:
        """return a list of indices for all characters whose first name starts with prefix"""
        

    def describe(self):
        """Return a multi-line string describing the cast."""
        lines = []
        for char in self.__underlying:
            lines.append(str(char))
        return "\n".join(lines)