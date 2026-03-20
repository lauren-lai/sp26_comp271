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
        __file_name = "queue.txt"
        self.__queue = open(file_name, "w")
        self.__queue.close()
    
    def enqueue(self, item: Any) -> None:
        with open(self.__file_name, "r") as f:
            existing = f.read()
        combined = item + existing
        with open(self.__file_name, "w") as f:
            f.write(combined)

    def dequeue(self) -> Any:
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
            f.writelines(lines[1:])

    def is_empty(self) -> bool:
        with open(self.__file_name, "r") as f:
            return f.read().strip() == None

    def size(self) -> int:
        with open(self.__file_name, "r") as f:
            return f.tell()

    def peek(self) -> Any:
        with open(self.__file_name, "r") as f:
            print(f.read())

class Stack(StackADT):
    
    def __init__():
        __file_name = "stack.txt"
        self.__stack = open(file_name, "w")
        self.__stack.close()

    def push(self, item: Any) -> None:
        with open(self.__file_name, "r") as f:
            existing = f.read()
        combined = item + existing
        with open(self.__file_name, "w") as f:
            f.write(combined)

    def pop(self) -> Any:
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
        with open(self.__file_name, "w") as f:
            f.writelines(lines[0, lines.len() - 1])

    def peek(self) -> Any:
        with open(self.__file_name, "r") as f:
            print(f.read())

    def is_empty(self) -> bool:
        with open(self.__file_name, "r") as f:
            return f.read().strip() == None

    def size(self) -> int:
        with open(self.__file_name, "r") as f:
            return f.tell()