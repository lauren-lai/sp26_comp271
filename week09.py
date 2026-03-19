from abc import ABC, abstractmethod
from __future__ import annotations
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
    
    def __init__():
        pass
    
    def enqueue(self, item: Any) -> None:
        pass

    def dequeue(self) -> Any:
        pass

    def is_empty(self) -> bool:
        pass

    def size(self) -> int:
        pass

    def peek(self) -> Any:
        pass

class Stack(StackADT):
    
    def __init__():
        pass

    def push(self, item: Any) -> None:
        pass

    def pop(self) -> Any:
        pass

    def peek(self) -> Any:
        pass

    def is_empty(self) -> bool:
        pass

    def size(self) -> int:
        pass