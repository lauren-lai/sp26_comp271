from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple, Type, Union

class QueueADT(ABC):
    @abstractmethod
    def enqueue(self, item: Any) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> Any:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def peek(self) -> Any:
        pass

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

class Queue(QueueADT):
    def __init__(self, capacity: int):
        self.__file_name = "queue.txt"
        self.__queue = open(file_name, "w")
        self.__queue.close()
    
    def enqueue(self, item: Any) -> None:
        """ adds the given item to the top of the file, keeping original content """
        with open(self.__file_name, "r") as f:
            existing = f.read()
        combined = item + existing
        with open(self.__file_name, "w") as f:
            f.write(combined)

    def dequeue(self) -> Any:
        """ removes and returns the first line from the file """
        to_return = None
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
            to_return = lines[0]
            f.writelines(lines[1:])
        return to_return

    def is_empty(self) -> bool:
        """ returns True if the file is empty, False otherwise """
        with open(self.__file_name, "r") as f:
            return f.read().strip() == None

    def size(self) -> int:
        """ returns the size of the file """
        with open(self.__file_name, "r") as f:
            f.seek(0, 2)
            return f.tell()

    def peek(self) -> Any:
        """ returns the file """
        with open(self.__file_name, "r") as f:
            return f.read()
class Stack(StackADT):
    def __init__():
        self.__file_name = "stack.txt"
        self.__stack = open(file_name, "w")
        self.__stack.close()

    def push(self, item: Any) -> None:
        """ adds item to the top of the file, keeping original content """
        with open(self.__file_name, "r") as f:
            existing = f.read()
        combined = item + existing
        with open(self.__file_name, "w") as f:
            f.write(combined)

    def pop(self) -> Any:
        """ removes and returns the last line of text from the file """
        to_return = None
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
            to_return = lines[lines.len() - 1]
        with open(self.__file_name, "w") as f:
            f.writelines(lines[0, lines.len() - 1])
        return to_return

    def peek(self) -> Any:
        """ returns the text of the file """
        with open(self.__file_name, "r") as f:
            return f.read()

    def is_empty(self) -> bool:
        """ returns True if the file is empty, False otherwise """
        with open(self.__file_name, "r") as f:
            return f.read().strip() == None

    def size(self) -> int:
        """ returns the size of the file """
        with open(self.__file_name, "r") as f:
            f.seek(0, 2)
            return f.tell()