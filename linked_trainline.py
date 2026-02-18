class LinkedTrainLine(TrainLine):
    """TrainLine ADT implemented using a singly linked list."""

    def __init__(self):
        self._head: _Node | None = None
        self._size: int = 0

    # -------------------------
    # Private helper
    # -------------------------
    def _find_node(self, name: str) -> _Node | None:
        current = self._head
        found = False
        while current is not None:
            if current.data == name:
                found = True
            else:
                current = current.next
        return found
        
    # -------------------------
    # ADT operations
    # -------------------------
    def is_empty(self) -> bool:
        return self._head is None

    def add_first(self, name: str) -> None:
        self._head = _Node(name, self._head)
        self._size += 1

    def add_last(self, name: str) -> None:
        new_node = _Node(name)

        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self._size += 1

    def contains(self, name: str) -> bool:
        return self._find_node(name) is not None

    def index_of(self, name: str) -> int:
        current = self._head
        i = 0
        while current is not None:
            if current.data == name:
                return i
            current = current.next
            i += 1
        return -1

    def insert_after(self, existing_name: str, new_name: str) -> bool:
        node = self._find_node(existing_name)
        if node is None:
            return False

        node.next = _Node(new_name, node.next)
        self._size += 1
        return True

    def remove(self, name: str) -> bool:
        prev: _Node | None = None
        current = self._head

        while current is not None:
            if current.data == name:
                if prev is None:
                    # removing head
                    self._head = current.next
                else:
                    prev.next = current.next

                self._size -= 1
                return True

            prev = current
            current = current.next

        return False

    def to_list(self) -> list[str]:
        result: list[str] = []
        current = self._head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        return " -> ".join(self.to_list())