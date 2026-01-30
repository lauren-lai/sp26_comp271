_FIRST_NAME = 0
_LAST_NAME = 1
_LAST_NAMEROLE = 2

def _contains_name(name: str, underlying: list[list[str]], index: int) -> bool:
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

def add(first_name: str, last_name :str, role: str, underlying: list[list[str]]) -> None:
    """
    creates a new entry in underlying of [first_name, last_name, role]
    """
    underlying.append([first_name, last_name, role])
    
def add_unique_first_name(first_name: str, last_name: str, role: str, underlying: list[list[str]]) -> None:
        """
        creates a new entry in underlying of [first_name,  last_name, role] if first_name isnt in underlying[_FIRST_NAME]
        """
        if not _contains_name(first_name, underlying, _FIRST_NAME):
            underlying.append([first_name, last_name, role])
    
def add_unique_last_name(first_name: str, last_name: str, role: str,underlying: list[list[str]]) -> None:
    """
    creates a new entry in underlying of [first_name, last_name, role] if last_name isnt in underlying[_LAST_NAME]
    """
    if not _contains_name( last_name, underlying, _LAST_NAME):
        underlying.append([first_name, last_name, role])
    
def remove_first_name(first_name: str, underlying: list[list[str]]) -> str|None:
    """
    removes first_name from underlying if present and returns first_name, otherwise returns None
    """
    removed: str = None
    have_removed: bool = False
    i: int = 0
    while (not have_removed) and (i < len(underlying)):
        if underlying[i][_FIRST_NAME] == first_name:
            removed = underlying.pop(i)
            have_removed = True
        i += 1
    return removed
        
def remove_all_first_name(first_name: str, underlying: list[list[str]]) -> list[str]|None:
    """
    removes all instances of first_name from underlying and returns a list of all instances, otherwise returns None
    """
    removed_names: list = []
    i: int = 0
    while i < len(underlying):
        name = remove_first_name(first_name, underlying)
        if name != None:
            removed_names.append(name)
        else:
            i += 1
    return removed_names if len(removed_names) > 0 else None

def main():
    _ST_CHARACTERS = [
        ["Jim", "Hopper", "Chief of Police"],
        ["Eleven", "", "Psychokinetic Overachiever"],
        ["Dustin", "Henderson", "Science Enthusiast"]
    ]
    print(f"ORIGINAL LIST = {_ST_CHARACTERS}")

    # testing adds:
    # add("Yuri", "Ismaylov", "Smuggler", _ST_CHARACTERS)
    # add_unique_first_name("Mike", "Wheeler", "annoying kid", _ST_CHARACTERS)
    # add_unique_last_name("Holly", "Wheeler", "goat", _ST_CHARACTERS)

    # testing removes:
    # remove_first_name("Jim", _ST_CHARACTERS)
    
    # add("Yuri", "Ismaylov", "Smuggler", _ST_CHARACTERS)
    # add("Yuri", "Ismaylov", "Smuggler", _ST_CHARACTERS)
    # remove_all_first_name("Yuri", _ST_CHARACTERS)

    print(f"FINAL LIST = {_ST_CHARACTERS}")

main()
