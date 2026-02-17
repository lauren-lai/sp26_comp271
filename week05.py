from abc import ABC, abstractmethod


class PantheonADT(ABC):
    """
    Pantheon ADT 

    Concept:
        A Pantheon stores a set of unique gods. Each god has:
            - a unique name (the key)
            - a domain (the value), e.g., "war", "wisdom", "harvest"

    ADT Rule (invariant):
        God names are unique. Domains do NOT need to be unique.
    """

    @abstractmethod
    def register(self, god_name: str, domain: str) -> bool:
        """
        Register a god into the pantheon.

        Parameters:
            god_name: unique identifier for the god (key)
            domain: the god's domain (value)

        Returns:
            True  if the god_name was not already present and was newly added.
            False if the god_name already existed (no changes made).

        Notes:
            - This operation does NOT overwrite existing entries.
            - Use change_domain(...) to update an existing god.
        """
        ...

    @abstractmethod
    def change_domain(self, god_name: str, new_domain: str) -> bool:
        """
        Change the domain of an already-registered god.

        Parameters:
            god_name: the god to update
            new_domain: the new domain to store

        Returns:
            True  if god_name exists and the update was performed.
            False if god_name does not exist (no changes made).
        """
        ...

    @abstractmethod
    def get_domain(self, god_name: str) -> str:
        """
        Retrieve the domain for a god.

        Parameters:
            god_name: the god to look up

        Returns:
            The domain (str) if the god exists; otherwise None.

        Important:
            - This method must NOT mutate the pantheon.
        """
        ...

    @abstractmethod
    def remove_god(self, god_name: str) -> bool:
        """
        Remove a god from the pantheon.

        Parameters:
            god_name: the god to remove

        Returns:
            True  if the god existed and was removed.
            False if the god was not found.
        """
        ...

    @abstractmethod
    def contains(self, god_name: str) -> bool:
        """
        Check whether a god is registered.

        Parameters:
            god_name: the god name to check

        Returns:
            True if present, otherwise False.
        """
        ...

    @abstractmethod
    def count(self) -> int:
        """
        Return the number of gods currently registered in the pantheon.
        """
        ...

    @abstractmethod
    def list_all(self):
        """
        Return a snapshot list of all registered gods and their domains.

        Returns:
            A NEW list of pairs, where each pair is [god_name, domain].

        Requirements:
            - Must return a copy (caller mutations must not affect internals).
            - Ordering is up to the implementation unless otherwise specified
              by a derived class / assignment variant.
        """