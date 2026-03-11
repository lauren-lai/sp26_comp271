
from __future__ import annotations
import unittest

# The following line requires the presence of file backpack.py in the same
# folder as this week07.py file.
from backpack import Backpack

# A new backpack starts empty.
# The default capacity is 5 when not specified.
# Adding items increases count() appropriately.
# Items are stored in insertion order.
# Adding when full returns False and does not change contents.
# Removing an existing item works and reduces count.
# Removing a missing item returns False and does not change contents.
# Duplicate items are allowed and removed one at a time.
# is_full() transitions correctly at the capacity boundary.
# items() returns a copy (mutating the returned list does not affect the backpack).
# __str__ output matches the specification exactly (both empty and non-empty cases).

class Test_Backpack(unittest.TestCase):
    # Remove the pass statement below and write your test methods
    # in this class
    def test_starts_empty(self):
        pass

    def test_default_capacity(self):
        pass

    def test_count_increments(self):
        pass

    def test_stores_in_order(self):
        pass

    def test_adding_when_full(self):
        pass

    def test_remove_works(self):
        pass

    def test_remove_decrements_count(self):
        pass

    def test_remove_missing_item(self):
        pass

    def test_allows_duplicate_items(self):
        pass

    def test_remove_one_duplicate_item(self):
        pass

    def test_is_full_changes(self):
        pass

    def test_items_returns_copy(self):
        pass

    def test_str_is_correct(self):
        pass




# ----- Run the tests
#
# If you test in a .PY file, uncomment TEST-LINE-1 and TEST-LINE-2 and
# comment out TEST-LINE-3 to run the tests.
#
# if __name__ == "__main__":              #   TEST-LINE-1
#   unittest.main()                       #   TEST-LINE-2
#
# If you test in a Jupyter notebook, comment out TEST-LINE-1 and TEST-LINE-2
# and uncomment TEST-LINE-C to run the tests in the notebook.
#
# unittest.main(argv=[''], exit=False)    #   TEST-LINE-3
#