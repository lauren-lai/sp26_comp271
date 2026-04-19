class WeirdoBST:
    def __init__(self):
        self.__underlying: list[str|None] = []

    def insert(self, value: str) -> None:
        """inserts a new value into the BST, assuming no duplicates"""
        # print("-----------------------------")
        current = 0
        parent = 0
        found = False
        # need case for first element
        if len(self.__underlying) == 0:
            self.__underlying.append(value)
            found = True
        elif self.__underlying[0] == value:
            found = True

        #tracking indexes because .left/.right isnt an option
        while self.__underlying[current] is not None and not found:
            # print("in while loop")
            if self.__underlying[current] == value:
                # print("in matching if")
                found = True
            parent = current
            if value < self.__underlying[current]:
                # print("in less than")
                current = (current * 2) + 1
            else:
                # print("in greater than")
                current = (current * 2) + 2
            # print(f"updated current is {current}")
            if current >= len(self.__underlying):
                for i in range(current):
                    self.__underlying.append(None)

        if current != 0:
            if value < self.__underlying[parent]:
                self.__underlying[parent*2 + 1] = value
            else:
                self.__underlying[parent*2 + 2] = value

    def search(self, value: str) -> bool:
        """returns whether the given string is present in the list"""
        i = 0
        current = self.__underlying[i]
        while current is not None:
            if current == value:
                return True
            elif value < current:
                current = self.__underlying[2*i + 1]
            else:
                current = self.__underlying[2*i + 2]
            i += 1
        return False

    def __len__(self) -> int:
        """returns the number of strings stored"""
        n = 0
        for i in range(len(self.__underlying)):
            if self.__underlying[i] is not None:
                n += 1
        return n

    _HEADER_FORMAT = "this tree has {} elements!"
    def __str__(self) -> str:
        """returns a print-friendly string"""
        output = self._HEADER_FORMAT.format(self.__len__())
        for i in range(len(self.__underlying)):
            output += f"\n\tat {i}, the value is {self.__underlying[i]}"
        return output
        

if __name__ == "__main__":
    bst = WeirdoBST()
    print(bst.__str__())

    # bst.insert("A")
    # bst.insert("B")
    # bst.insert("C")
    # bst.insert("D")

    bst.insert("Z")
    bst.insert("M")
    bst.insert("F")

    print(bst.__len__())
    print(bst.search("Z")) # should print True
    print(bst.search("O")) # should print False
    
    print(bst.__str__())
