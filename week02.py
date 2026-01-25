class Week02:

    def contains_name(self, name: str, underlying: list[list[str]], index: int) -> bool:
        """
        returns True if underlying contains name in the sublist index of underlying
        """
        is_found: bool = False
        i: int = 0
        while (not is_found) and (i < len(underlying)):
            if (underlying[i][index] == name):
                is_found = True
            i += 1
        return is_found

    def add(self, first_name: str, last_name:str, role: str, underlying: list[list[str]]) -> None:
        underlying.append([first_name, last_name, role])
    
    def add_unique_first_name(self, first_name: str, last_name:str, role: str,underlying: list[list[str]]) -> None:
        if not contains_name(first_name, underlying, 0):
            underlying.append([first_name, last_name, role])
    
    def add_unique_last_name(self, first_name: str, last_name:str, role: str,underlying: list[list[str]]) -> None:
        if not contains_name(last_name, underlying, 1):
            underlying.append([first_name, last_name, role])
    
    def remove_first_name(self, first_name: str, underlying: list[list[str]]) -> str|None:
        """
        removes first_name from underlying if present and returns first_name, otherwise returns None
        """
        removed: str = None
        have_removed: bool = False
        i: int = 0

        while (not have_removed) and (i < len(underlying)):
            if underlying[i][0] == first_name:
                removed = underlying[i][0]
                have_removed = True
            i += 1

        return removed
        

    def remove_all_first_name(self, first_name: str, underlying: list[list[str]]) -> list[str]|None:
        """
        removes all instances of first_name from underlying and returns a list of all instances, otherwise returns None
        """
        removed: list = []
        i: int = 0

        while i < len(underlying):
            if underlying[i][0] == first_name:
                removed.append(underlying[i][0])
                underlying.pop(i)
            else:
                i += 1

        return removed


class Main():
    _ST_CHARACTERS = [
        ["Jim", "Hopper", "Chief of Police"],
        ["Eleven", "", "Psychokinetic Overachiever"],
        ["Dustin", "Henderson", "Science Enthusiast"]
    ]
    week02 = Week02()

    week02.add("Yuri", "Ismaylov", "Smuggler", _ST_CHARACTERS)
    week02.add("Yuri", "Ismaylov", "Smuggler", _ST_CHARACTERS)
    week02.add("Yuri", "Ismaylov", "Smuggler", _ST_CHARACTERS)

    print(_ST_CHARACTERS)
    str = week02.remove_all_first_name("Yuri", _ST_CHARACTERS)
    print(str)
    # week02.add_unique_first_name("yuri", "ismaylov", "smuggler", _ST_CHARACTERS)
    # week02.add_unique_last_name("yuri", "ismaylov", "smuggler", _ST_CHARACTERS)
    # week02.remove_first_name("yuri", "ismaylov", "smuggler", _ST_CHARACTERS)
    # week02.remove_first_name("yuri", "ismaylov", "smuggler", _ST_CHARACTERS)


