from __future__ import annotations

import random
import string
class ProbingHashTable:
    """Hash table demonstrating linear vs. quadratic probing."""

    # Consstants for default values and error messages
    _DEFAULT_CAPACITY: int = 11
    _PROBE_MODES: tuple[str, str] = ("linear", "quadratic")
    _DEFAULT_PROBING_MODE: str = _PROBE_MODES[0]
    _ERROR_MODE: str = f"mode must be one of {', '.join(_PROBE_MODES)}"
    _ERROR_FULL: str = "Hash table is full"

    def __init__(
        self, capacity: int = _DEFAULT_CAPACITY, mode: str = _DEFAULT_PROBING_MODE
    ):
        """Initialize the hash table with the given capacity and probing mode."""
        if mode not in self._PROBE_MODES:
            # If the mode is not valid,
            # use default mode.
            mode = self._DEFAULT_PROBING_MODE
        self._capacity = capacity
        self._mode = mode
        # Each slot is a string or None
        self._table: list[str | None] = [None] * capacity
        self._size = 0

    def _hash(self, key: int) -> int:
        """Convert an integer value to an index in the underlying table."""
        return key % self._capacity

    def _probe(self, position: int, attempt: int) -> int:
        """"""
        if self._mode == self._DEFAULT_PROBING_MODE:  # linear
            return (position + attempt) % self._capacity
        else:  # quadratic
            return (position + attempt * attempt) % self._capacity

    def load_factor(self) -> float:
        """Return the current load factor of the hash table."""
        return self._size / self._capacity

    def insert(self, value: str) -> list[int]:
        """Insert key-value pair. Returns list of indices probed."""
        # Initialize list to track probe indices
        probes: list[int] = []
        # Check if the hash table has space for a new entry.
        # If not, we will not attempt to insert and will return
        # an empty list of probes.
        if self._size < self._capacity:
            # Generate a non-negative integer key from the value
            key: int = abs(hash(value))
            # Convert the key to an index in the underlying table
            index: int = self._hash(key)
            # Attempt to insert the key-value pair, probing for an empty
            # slot.
            i: int = 0
            insertion_successful: bool = False
            # Loop to attempt to find an empty slot. The loop ends as soon as
            # we have probed the entire table or successfully inserted the
            # value.
            while i < self._capacity and not insertion_successful:
                # Location in the underlying table to check
                probe_index: int = self._probe(index, i)
                # Record the location we are probing
                probes.append(probe_index)
                # Obtain the contents at the location we are probing
                slot: str | None = self._table[probe_index]
                # Determine if we can insert the value at the location we are probing.
                # If insertion is successful, we will exit the loop. If not, we will
                # try the next probe index in the next iteration of the loop.
                insertion_successful = slot is None or slot == value
                if insertion_successful:
                    # The slot is empty or contains the same value already,
                    # so we can insert the value pair here (or update the existing
                    # value if it is the same).
                    self._table[probe_index] = value
                    if slot is None:
                        # Update the size of the hash table if we added
                        # this value for the first time, ie, we have not
                        # overwriten it.
                        self._size += 1
                # If the slot is not empty, we will try the next probe index
                # in the next iteration of the loop.
                i += 1
        return probes

    def contains(self, value: str) -> bool:
        """Check if value is in the hash table."""
        # Generate a non-negative integer key from the value
        key: int = abs(hash(value))
        # Convert the key to an index in the underlying table
        index: int = self._hash(key)
        # Loop to probe for the value. The loop ends as soon as we have probed the
        # entire table or found the value.
        found: bool = False
        i: int = 0
        # Loop ends when we have probed the entire table or found the value
        while i < self._capacity and not found:
            probe_index: int = self._probe(index, i)
            slot: str | None = self._table[probe_index]
            if slot is not None:
                found = slot == value
            i += 1
        return found

    # Formating constants for display
    _FMT_HEADER: str = f"{'Idx':<5}{'Content'}"
    _FMT_EMPTY: str = "---"
    _FMT_SLOT: str = "{idx:5} -> {content}"
    _FMT_HORIZONTAL: str = "-" * 20

    def display(self) -> str:
        """Return a string representation of the hash table."""
        lines: list[str] = [self._FMT_HEADER]
        lines.append(self._FMT_HORIZONTAL)
        for i in range(self._capacity):
            slot: str | None = self._table[i]
            content: str = (
                self._FMT_SLOT.format(idx=i, content=slot) if slot else self._FMT_EMPTY
            )
            lines.append(content)
        return "\n".join(lines)

class TestHashTable:

    def __init__(self, hash_table: ProbingHashTable):
        self._hash_table = hash_table
        self._table_modes = hash_table._PROBE_MODES
        self._table_capacity = hash_table._DEFAULT_CAPACITY
    
    def random_string(self, n: int) -> str:
        """Generate a random string of length n using alphabetical characters."""
        return "".join(random.choices(string.ascii_letters, k=n))

    def test(self, trials: int, mode: str) -> [[]]:
        """Demonstrate linear and quadratic probing with random string insertions."""
        # print(f"\n{'=' * 40}")
        # print(f"  {mode.upper()} PROBING ({self._table_capacity})")
        # print(f"{'=' * 40}")

        probe_lf_table = [[]]
        
        for _ in range(trials):
            value: str = self.random_string(5)
            probes: list[int] = self._hash_table.insert(value)
            status: str = "collision!" if len(probes) > 1 else "direct"
            # print(
            #     f"  insert({value}): hash={abs(hash(value)) % capacity:<3} probes={probes}  [{status}]"
            # )
            load_factor = round(self._hash_table._size / self._hash_table._capacity, 2) # couldn't get the :.2f to work here
            probe_lf_table.append([len(probes), load_factor])

        # print(f"\n{self._hash_table.display()}")
        # print(
        #     f"\nLoad factor: {self._hash_table._size}/{self._hash_table._capacity} = {self._hash_table._size / self._hash_table._capacity:.2f}"
        # )

        return probe_lf_table


if __name__ == "__main__":
        
    capacity = 11
    modes: tuple[str, str] = ("linear", "quadratic")
    trials = 10 # number of tests
    reps = 11 # number of strings generated per test

    linear_results = [[]]
    quadratic_results = [[]]

    for mode in modes:
        print("*" * 80)
        for i in range(trials):
            ht = TestHashTable(ProbingHashTable(capacity, mode))
            results = ht.test(reps, mode)
            linear_results.append(results) if mode == modes[0] else quadratic_results.append(results)

    print(f"LINEAR TEST RESULTS: \n\t{linear_results}")
    print(f"QUADRATIC TEST RESULTS: \n\t{quadratic_results}")

    
