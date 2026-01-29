class Week02:
    _FIRST_NAME = 0
    _LAST_NAME = 1
    _ROLE = 2

    def _contains_name(self, name: str, underlying: list[list[str]], index: int) -> bool:
        """
        returns True if underlying contains name in the sublist index of underlying, False otherwise
        """
        is_found: bool = False
        i: int = 0
        while (not is_found) and (i < len(underlying)):
            if (underlying[i][index] == name):
                is_found = True
            i += 1
        return is_found

    def add(self, first_name: str, last_name :str, role: str, underlying: list[list[str]]) -> None:
        """
        creates a new entry in underlying of [first_name, last_name, role]
        """
        underlying.append([first_name, last_name, role])
    
    def add_unique_first_name(self, first_name: str, last_name: str, role: str, underlying: list[list[str]]) -> None:
        """
        creates a new entry in underlying of [first_name,  last_name, role] if first_name isnt in underlying[0]
        """
        if not self.contains_name(first_name, underlying, self._FIRST_NAME):
            underlying.append([first_name, last_name, role])
    
    def add_unique_last_name(self, first_name: str, last_name: str, role: str,underlying: list[list[str]]) -> None:
        """
        creates a new entry in underlying of [first_name, last_name, role] if last_name isnt in underlying[1]
        """
        if not self.contains_name( last_name, underlying, self._LAST_NAME):
            underlying.append([first_name, last_name, role])
    
    def remove_first_name(self, first_name: str, underlying: list[list[str]]) -> str|None:
        """
        removes first_name from underlying if present and returns first_name, otherwise returns None
        """
        removed: str = None
        have_removed: bool = False
        i: int = 0
        while (not have_removed) and (i < len(underlying)):
            if underlying[i][self._FIRST_NAME] == first_name:
                removed = underlying.pop(i)
                have_removed = True
            i += 1
        return removed
        
    def remove_all_first_name(self, first_name: str, underlying: list[list[str]]) -> list[str]|None:
        """
        removes all instances of first_name from underlying and returns a list of all instances, otherwise returns None
        """
        removed_names: list = []
        i: int = 0
        while i < len(underlying):
            name = self.remove_first_name(first_name, underlying)
            if name != None:
                removed_names.append(name)
            else:
                i += 1
        return removed_names

class Main():
    _ST_CHARACTERS = [
        ["Jim", "Hopper", "Chief of Police"],
        ["Eleven", "", "Psychokinetic Overachiever"],
        ["Dustin", "Henderson", "Science Enthusiast"]
    ]
    week02 = Week02()
    print(f"ORIGINAL LIST = {_ST_CHARACTERS}")

    # testing adds:
    # week02.add("Yuri", "Ismaylov", "Smuggler", _ST_CHARACTERS)
    # week02.add_unique_first_name("Yuri", "Ismaylov", "Smuggler", _ST_CHARACTERS)
    # week02.add_unique_last_name("Yuri", "Ismaylov", "Smuggler", _ST_CHARACTERS)

    # testing removes:
    # week02.remove_first_name("Jim", _ST_CHARACTERS)
    
    # week02.add("Yuri", "Ismaylov", "Smuggler", _ST_CHARACTERS)
    # week02.add("Yuri", "Ismaylov", "Smuggler", _ST_CHARACTERS)
    # week02.remove_all_first_name("Yuri", _ST_CHARACTERS)

    print(f"FINAL LIST = {_ST_CHARACTERS}")

