from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Type, Union

class StackADT(ABC):
    @abstractmethod
    def push(self, item: Any) -> None:
        pass

    @abstractmethod
    def pop(self) -> Any:
        pass

    @abstractmethod
    def peek(self) -> Any:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

class Stack(StackADT):
    """Array-backed stack using Python list as the underlying store."""

    def __init__(self):
        self._data = []          # right end of list = top of stack

    def push(self, item):
        """O(1) amortised — append to the right end."""
        self._data.append(item)

    def pop(self):
        """O(1) — remove and return the top element."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        """O(1) — inspect without removing."""
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data} ← top)"


# ── Demo ──────────────────────────────────────────
def demo_Stack():
    s = Stack()
    for val in [99, 5, 17, 42]:
        s.push(val)
    
    print(s)          # Stack([99, 5, 17, 42] ← top)
    print(s.peek())   # 42
    print(s.pop())    # 42
    print(s.pop())    # 17
    print(len(s))     # 2

demo_Stack()






class FixedStack:
    """Stack backed by a fixed-size list. Raises if capacity is exceeded."""

    def __init__(self, capacity: int = 10):
        self._capacity = capacity
        self._data = [None] * capacity   # pre-allocate
        self._top = -1                   # -1 means empty

    def push(self, item):
        """ 
        If the stack has reached its capacity, raise an Overflow Error
        Otherwise, add to the right end item and update the top of the Stack.
        """
        pass

    def pop(self):
        """ 
        If the stack is empty, raise an Index Error.
        Otherwise, delete the item at the top of the Stack, update the top and return the item.
        """
        # After a pop, setting the freed slot to None lets Python's garbage collector reclaim objects that are no longer logically in the stack. 
        # Skipping this step can cause subtle memory leaks when storing large objects.

        pass

    def peek(self):
        """ 
        If the stack is empty, raise an Index Error.
        Otherwise, return the item at the top of the stack.
        """
        pass

    def is_empty(self):
        return self._top == -1

    def __len__(self):
        return self._top + 1

    def clear(self):
        self._data = [None] * self._capacity
        self._top = -1

def demo_FixedStack(): 
    fs = FixedStack(capacity=5)

    fs.push(10)   # _data: [10, None, None, None, None]   _top: 0
    fs.push(20)   # _data: [10,  20,  None, None, None]   _top: 1
    fs.push(30)   # _data: [10,  20,   30,  None, None]   _top: 2
    
    fs.pop()      # returns 30  — _top: 1
    fs.pop()      # returns 20  — _top: 0
    fs.peek()     # returns 10  — _top unchanged: 0

demo_FixedStack()


class Stack:
    """Array-backed stack using Python list as the underlying store."""

    def __init__(self):
        self._data = []          # right end of list = top of stack

    def push(self, item):
        """O(1) amortised — append to the right end."""
        self._data.append(item)

    def pop(self):
        """O(1) — remove and return the top element."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        """O(1) — inspect without removing."""
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data} ← top)"


# ── Demo ──────────────────────────────────────────
s = Stack()
for val in [99, 5, 17, 42]:
    s.push(val)

print(s)          # Stack([99, 5, 17, 42] ← top)
print(s.peek())   # 42
print(s.pop())    # 42
print(s.pop())    # 17
print(len(s))     # 2