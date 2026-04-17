class Node:

    """A node in a linked list."""
    
    def __init__(self, value):
        self.__value = value
        self.__next = None

    def __str__(self):
        return str(self.__value)

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next

    def has_next(self):
        return self.__next != None

class LinkedList:
    """A simple linked list data structure."""

    def __init__(self):
        # Fields below are designated as protected (single
        # unferscore) instead of private (double underscore).
        # The objective is still to show other users that 
        # the fields are for internal-use only. And at the 
        # same time to avoid the complications from double
        # underscore name mangling.
        self._head = None
        self._tail = None
        self._size = 0

    def __str__(self):
        """Tragically simple string rendering"""
        result = ""
        current = self._head
        while current != None:
            result += str(current) + " "
            current = current.get_next()
        return result

    def add(self, new_node: Node) -> None:
        """Adds a new node to the linked list."""
        if new_node is not None:
            # Operate only if there is something given to
            # us to add.
            if self._head == None:
                self._head = new_node
            else:
                self._tail.set_next(new_node)
            # In either case, update the tail
            self._tail = new_node
            # Update the size of the object
            self._size += 1
    
    def add_with_string(self, value:str) -> None:
        if value is not None:
            self.add(Node(value))

    def remove(self, value:str) -> bool:
        current = self._head
        if current is None:
            return False
        # only head in list
        if current.get_value() == value:
            self._head = current.get_next()
            current = None
            return True

        previous = None
        found = False
        while current.get_next() is not None and not found:
            previous = current
            current = current.get_next()
            if current.get_value() == value:
                previous.set_next(current.get_next())
                found = True

        if current.get_next() is None and current.get_value() == value:
            current = None
            found = True
        
        return found



        
    def remove_all(self, value:str) -> bool:
        pass


# -------------------------
# Brutally naive testing
# -------------------------
if __name__ == "__main__":
    test = LinkedList()
    for i in range(10):
        test.add(Node(i))
    print(test)

    test2 = LinkedList()
    print(test2.remove(3))

    print(test.remove(5))
    print(test.remove(9))
    print(test.remove(10))
    print(test.remove(0))
    print(test)
