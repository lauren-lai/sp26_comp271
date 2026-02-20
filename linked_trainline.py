from __future__ import annotations
from abc import ABC, abstractmethod


class TrainLine(ABC):
    """ADT for an ordered collection of stations."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Return True if the train line has no stations."""
        raise NotImplementedError

    @abstractmethod
    def add_first(self, name: str) -> None:
        """Add a station at the beginning of the line."""
        raise NotImplementedError

    @abstractmethod
    def add_last(self, name: str) -> None:
        """Add a station at the end of the line."""
        raise NotImplementedError

    @abstractmethod
    def contains(self, name: str) -> bool:
        """Return True iff a station with this name appears in the line."""
        raise NotImplementedError

    @abstractmethod
    def index_of(self, name: str) -> int:
        """Return the position of the first matching station, or -1 if not found."""
        raise NotImplementedError

    @abstractmethod
    def insert_after(self, existing_name: str, new_name: str) -> bool:
        """Insert new_name right after the first occurrence of existing_name.

        Returns:
            True if inserted successfully; False if existing_name not found.
        """
        raise NotImplementedError

    @abstractmethod
    def remove(self, name: str) -> bool:
        """Remove the first occurrence of name from the line.

        Returns:
            True if removed successfully; False if not found.
        """
        raise NotImplementedError

    @abstractmethod
    def to_list(self) -> list[str]:
        """Return station names in order as a Python list (useful for testing)."""
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        """Return the number of stations."""
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        """Return a human-readable representation of the line."""
        raise NotImplementedError


class _Node:
    """Internal node for a singly linked list."""

    __slots__ = ("data", "next")

    def __init__(self, data: str, next_node: _Node | None = None) -> None:
        self.data: str = data
        self.next: _Node | None = next_node

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
        """ return True iff a station with this name appears in the line """
        current = self._head
        found = False
        while (current is not None) and (not found):
            if name  == curent.data:
                found = True
            else:
                curent = current.next
        return found

    def index_of(self, name: str) -> int:
        """ returns the index of the node name, returns -1 if not"""
        current = self._head
        i = 0
        index = -1
        while (current is not None) and (index == -1): # iterates until end of list or name is found
            if current.data == name:
                index = i
            else:
                current = current.next
                i += 1
        return index

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