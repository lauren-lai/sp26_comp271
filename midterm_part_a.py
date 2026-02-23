class Node:
    """A simple linkable object. The node comprises two fields: a value field,
    here typed a string, and a pointer field to the next node. The default is
    to instantiate a node with just a value, and no other node to point to it,
    for example:

    +------+
    | node |-next--> None
    +------+

    Nodes are connected to each other later, for example,

    chi = Node("Chicago")        spi = Node("Springfield")
    +------+                     +------+
    | node |-next--> None        | node |-next--> None
    +------+                     +------+

    and then chi.set_next(spi) will result to the arrangement below which is,
    essentially, a linked list.

    chi -----------------------> spi

    +------+                     +------+
    | node |-next--------------> | node |-next--> None
    +------+                     +------+

    """

    def __init__(self, value: str) -> None:
        """Object constructor. Requires only a value to instantiate the object.
        The next object may be assigned later"""
        self.__value: str = value
        self.__next: Node | None = None

    def __str__(self) -> str:
        """Simple string representation of the object."""
        return f"{self.__value}"

    def has_next(self) -> bool:
        """Predicate accessor; tells if object points to
        another object"""
        return self.__next is not None

    def get_next(self) -> Node | None:
        """Standard accessor for next object"""
        return self.__next

    def set_next(self, next: Node) -> None:
        """Mutates object by assigning its next pointer to another object"""
        self.__next = next

    def get_value(self) -> str:
        """Accessor for the object's value"""
        return self.__value


class LinkedList:
    """A simple linked list of Node objects. Nodes in this list are
    connected one after the other, as shown below

      head
    +------+         +------+         +------+        +------+
    | node |-next--> | node |-next--> | node |--> ... | node |-next-->  None
    +------+         +------+         +------+        +------+

    Every node, in the linked list, is connected to another node. Except for
    the last node that points to None.
    """

    def __init__(self) -> None:
        """Instantiate an empty linked list"""
        self.__head: Node | None = None

    # Constants for string representation of the linked list
    __EMPTY_LIST_STR: str = "Empty List"
    __RIGHT_ARROW: str = " → "

    def __str__(self) -> str:
        """String representation."""
        # Assume an empty list
        string: str = self.__EMPTY_LIST_STR
        if self.__head is not None:
            # If the list is not empty, we start with the head node and
            # we keep adding the value of the next node, until we reach
            # the end of the list.
            string = self.__head.get_value()
            # Start with the first node and keep adding the next node
            # until we reach the end of the list.
            current: Node = self.__head.get_next()
            while current is not None:
                # Add the next node to the string and move to the next
                # node. The loop ends when we reach the end of the list
                # and current is None.
                string += self.__RIGHT_ARROW + current.get_value()
                current = current.get_next()
        return string

    def add(self, value: str) -> None:
        """Adds a new node to the linked list. First we create a new node
        with the given value. And next we find the end of the linked list
        and we append the new node to it."""
        # Create the new node to be added
        new_node: Node = Node(value)
        # Determine if the linked list is empty.
        if self.__head is None:
            # If the list is empty, the new node becomes its head and
            # we are done.
            self.__head = new_node
        else:
            # If the list is not empty, find its last Node and add the new
            # Node object after it. To find the last Node, we start at the
            # head node, and move to the next node, until we find the node
            # whose next pointer is none.
            current: Node = self.__head
            # Look repeates as long as the current node has a next node
            # for us to slide to.
            while current.has_next():
                # Move to the next node and try again
                current = current.get_next()
            # At the time the loop ends, current is at the last node of the
            # linked list. Now we place the new node after the current node
            # and we are done.
            current.set_next(new_node)

    def count(self) -> int:
        """Counts the number of nodes in the object and returns it"""
        # Initialize the return item
        counter: int = 0
        # Start at the beginning of the linked list
        current: Node = self.__head
        # Go through every node, increasing the counter, until we
        # reach the last node and it takes out outside the linked list
        while current is not None:
            counter += 1
            current = current.get_next()
        return counter