class Week02:

    def add(self, first_name: str, last_name:str, role: str, underlying: list[list[str]]) -> None:
        print("add method")
    
    def add_unique_first_name(self, first_name: str, last_name:str, role: str,underlying: list[list[str]]) -> None:
        print("add unique first name method")
    
    def add_unique_last_name(self, first_name: str, last_name:str, role: str,underlying: list[list[str]]) -> None:
        print("add unique last name method")
    
    def remove_first_name(self, first_name: str, underlying: list[list[str]]) -> str|None:
        print("remove first name method")

    def remove_all_first_name(self, first_name: str, underlying: list[list[str]]) -> list[str]|None:
        print("remove all first name")


class Main():
    _ST_CHARACTERS = [
        ["Jim", "Hopper", "Chief of Police"],
        ["Eleven", "", "Psychokinetic Overachiever"],
        ["Dustin", "Henderson", "Science Enthusiast"]
    ]
    week02 = Week02()

    week02.add("yuri", "ismaylov", "smuggler", _ST_CHARACTERS)
    # week02.add_unique_first_name("yuri", "ismaylov", "smuggler", _ST_CHARACTERS)
    # week02.add_unique_last_name("yuri", "ismaylov", "smuggler", _ST_CHARACTERS)
    # week02.remove_first_name("yuri", "ismaylov", "smuggler", _ST_CHARACTERS)
    # week02.remove_first_name("yuri", "ismaylov", "smuggler", _ST_CHARACTERS)


