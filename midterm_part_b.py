from __future__ import annotations  # Authorized import for advanced type hints
from abc import ABC, abstractmethod  # Authorized import for derived classes

# 345678901234567890123456789012345678901234567890123456789012345678901234567890

class Performance(ABC):
    """
    A general live performance event.

    This class captures the shared structure and behavior of all
    live performances: concerts, lectures, theater productions,
    magic shows, etc.

    The purpose of this class is to define:

        • Common data that every performance has.
        • Common behavior shared by all performances.
        • A contract (via abstract methods) that subclasses must fulfill.

    Subclasses are responsible for defining how revenue is calculated
    and how the performance is described.
    """

    def __init__(
        self, title: str, duration_minutes: int, base_ticket_price: float
    ) -> None:
        """
        Initialize a new performance.

        Parameters:
            title               The name of the event.
            duration_minutes    How long the event lasts.
            base_ticket_price   The standard ticket price before
                                any subclass-specific adjustments.

        Note:
            We use protected attributes (_name style) instead of
            private (__name) because subclasses will need direct
            access to these values.
        """
        self._title: str = title
        self._duration_minutes: int = duration_minutes
        self._base_ticket_price: float = base_ticket_price

        # Number of audience members currently admitted.
        # Starts at zero and increases via admit_audience().
        self._audience_count: int = 0

    # ---------------------------------------------------------
    # Concrete (Fully Implemented) Methods
    # These are inherited as-is by subclasses.
    # ---------------------------------------------------------

    def __str__(self) -> str:
        """
        General string representation.

        We call describe() here so that when a Performance
        object is printed, the subclass version of describe()
        is used automatically (polymorphism in action).
        """
        return self.describe()

    def admit_audience(self, number: int) -> None:
        """
        Adds audience members to the performance.

        Only positive numbers are accepted.
        """
        if number > 0:
            self._audience_count += number

    def get_title(self) -> str:
        """Returns the performance title."""
        return self._title

    def get_duration(self) -> int:
        """Returns the duration in minutes."""
        return self._duration_minutes

    def get_audience_count(self) -> int:
        """Returns the number of admitted audience members."""
        return self._audience_count

    def get_base_ticket_price(self) -> float:
        """
        Returns the base ticket price.

        Subclasses may use this value as the starting point
        for their own pricing logic.
        """
        return self._base_ticket_price

    # ---------------------------------------------------------
    # Abstract Methods (Must Be Implemented by Subclasses)
    # ---------------------------------------------------------

    @abstractmethod
    def calculate_revenue(self) -> float:
        """
        Compute total revenue for the performance.

        Subclasses decide how ticket price is adjusted
        (VIP upgrades, student discounts, special pricing, etc.).

        The result should reflect:
            audience_count × adjusted_ticket_price
        """
        ...

    @abstractmethod
    def describe(self) -> str:
        """
        Return a human-readable description of the performance.

        Each subclass should include details specific
        to its type of event.
        """