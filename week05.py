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

class Deities(PantheonADT):
    """
    Pantheon ADT 

    Concept:
        A Pantheon stores a set of unique gods. Each god has:
            - a unique name (the key)
            - a domain (the value), e.g., "war", "wisdom", "harvest"

    ADT Rule (invariant):
        God names are unique. Domains do NOT need to be unique.
    """

    def __init__(self):
        self.__pantheon = {} # using the python dictoinary class

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
        updated = False
        if self.__pantheon.get(god_name) == None:
            self.__pantheon.update({god_name: domain})
            updated = True
        
        return updated
        

    def contains(self, god_name: str) -> bool:
        """
        Check whether a god is registered.

        Parameters:
            god_name: the god name to check

        Returns:
            True if present, otherwise False.
        """
        contains = False
        for key in self.__pantheon.keys():
            if key == god_name:
                contains = True

        return contains

    def get_domain(self, god_name: str) -> str | None:
        """
        Retrieve the domain for a god.

        Parameters:
            god_name: the god to look up

        Returns:
            The domain (str) if the god exists; otherwise None.

        Important:
            - This method must NOT mutate the pantheon.
        """
        return self.__pantheon.get(god_name) # returns None if key doesnt exist

        
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
        changed = False
        if self.contains(god_name):
            self.__pantheon.update({god_name: new_domain})
            changed = True
        
        return changed

    def remove_god(self, god_name: str) -> bool:
        """
        Remove a god from the pantheon.

        Parameters:
            god_name: the god to remove

        Returns:
            True  if the god existed and was removed.
            False if the god was not found.
        """
        removed = False
        if self.contains(god_name):
            self.__pantheon.pop(god_name)
            removed = True
        
        return removed

    def count(self) -> int:
        """
        Return the number of gods currently registered in the pantheon.
        """
        return len(self.__pantheon)

    def list_all(self) -> []:
        """
        Return a snapshot list of all registered gods and their domains.

        Returns:
            A NEW list of pairs, where each pair is [god_name, domain].

        Requirements:
            - Must return a copy (caller mutations must not affect internals).
            - Ordering is up to the implementation unless otherwise specified
              by a derived class / assignment variant.
        """
        to_return = []

        for key in self.__pantheon.keys():
            to_return.append([key, self.__pantheon.get(key)])

        return to_return




# ---------------------------
# Test code for PantheonADT / Deities
# ---------------------------


def check(label: str, expected, actual) -> None:
    ok = expected == actual
    print(f"{' Y ' if ok else ' N '} {label}") # had to change, emojis were throwing "UnicodeEncodeError: 'charmap' codec can't encode character '\u2705' in position 0: character maps to <undefined>""
    if not ok:
        print(f"   expected: {expected}")
        print(f"   actual:   {actual}")


def check_true(label: str, value: bool) -> None:
    check(label, True, value)


def check_false(label: str, value: bool) -> None:
    check(label, False, value)

def main() -> None:
    p = Deities()

    print("\n--- Basic empty state ---")
    check("count starts at 0", 0, p.count())
    check_false("contains('Ares') is False", p.contains("Ares"))
    check("get_domain('Ares') is None", None, p.get_domain("Ares"))
    check("list_all empty list", [], p.list_all())

    print("\n--- Register gods (unique keys) ---")
    check_true("register Ares/war succeeds", p.register("Ares", "war"))
    check_true("register Athena/wisdom succeeds", p.register("Athena", "wisdom"))
    check_true("register Demeter/harvest succeeds", p.register("Demeter", "harvest"))

    print(p.count())

    # duplicate key should not overwrite
    check_false(
        "register Ares/peace fails (duplicate key)", p.register("Ares", "peace")
    )
    check("Ares domain still 'war'", "war", p.get_domain("Ares"))

    print("\n--- Contains / Get domain ---")
    check_true("contains('Athena')", p.contains("Athena"))
    check_false("contains('Zeus')", p.contains("Zeus"))
    check("get_domain('Athena')", "wisdom", p.get_domain("Athena"))
    check("get_domain('Zeus') is None", None, p.get_domain("Zeus"))


    print("\n--- Change domain ---")
    check_true(
        "change_domain Athena -> strategy succeeds",
        p.change_domain("Athena", "strategy"),
    )
    check("Athena now 'strategy'", "strategy", p.get_domain("Athena"))
    check_false("change_domain Zeus -> sky fails", p.change_domain("Zeus", "sky"))

    print("\n--- Remove ---")
    check_true("remove_god Demeter succeeds", p.remove_god("Demeter"))
    check_false("remove_god Demeter again fails", p.remove_god("Demeter"))
    check_false("contains('Demeter') now False", p.contains("Demeter"))
    check("get_domain('Demeter') now None", None, p.get_domain("Demeter"))

    print("\n--- Snapshot behavior of list_all (copy) ---")
    snapshot = p.list_all()
    print("snapshot:", snapshot)

    # mutate returned list; should NOT affect internal list structure
    snapshot.append(["Zeus", "sky"])
    check_false(
        "after snapshot append, contains('Zeus') still False", p.contains("Zeus")
    )

    # mutate an inner pair in the snapshot; should NOT affect internals if deep-copied
    # (This is a great ADT test: list_all should protect internals.)
    if len(snapshot) > 0:
        snapshot[0][1] = "UNDERWORLD???"

        # Re-fetch domain for whatever god is at snapshot[0][0]
        god = snapshot[0][0]
        domain_now = p.get_domain(god)
        print(f"\n !! after snapshot inner-mutation, get_domain('{god}') -> {domain_now}") # had to change the emojis again same error as above
        print(f"                                  ===================== ^^^^^^^^^^^")
        print(f'                                  !! NOTE: If you see "UNDERWORLD??",')
        print(f'                                  above instead of \"war\", it means that')
        print(f"                                  list_all is not working properrly: it")
        print(
            f"                                  returns aliases instead of copies of pairs."
        )

    print("\n--- Final state ---")
    print("list_all:", p.list_all())
    print("count(): ", p.count())
    print("\nDone.")


if __name__ == "__main__":
    main()