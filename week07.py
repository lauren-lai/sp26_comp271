
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

    def test_initializes_empty(self):
        test_object:Backpack = Backpack("Lauren", 3)
        self.assertEqual("Backpack(owner=Lauren, items=empty)", test_object.str())

    def test_default_capacity(self):
        test_object:Backpack = Backpack("Lauren")
        test_object.add("Pencil")
        self.assertEqual("Backpack(owner=Lauren, items=1/5)", test_object.str())

    def test_count_increments(self):
        test_object:Backpack = Backpack("Lauren", 3)
        prev_count = test_object.count()

        result = test_object.add("Pencil")
        new_count = test_object.count()

        self.assertTrue(result)
        self.assertGreater(new_count, prev_count)        

    def test_stores_in_order(self):
        test_object:Backpack = Backpack("Lauren", 3)
        test_object.add("Pencil")
        test_object.add("Pen")
        items = test_object.items()

        self.assertEqual("[Pencil, Pen]", items)

    def test_adding_when_full(self):
        test_object:Backpack = Backpack("Lauren", 2)
        test_object.add("Pencil")
        test_object.add("Pen")
        prev_items = test_object.items()
        prev_count = test_object.count()

        test_object.add("Water")
        new_items = test_object.items()
        new_count = test_object.count()
        is_full = test_object.is_full()

        self.assertEqual(prev_count, new_count)
        self.assertTrue(is_full)
        self.assertTrue(prev_items, new_items)

    def test_remove(self):
        test_object:Backpack = Backpack("Lauren", 2)
        test_object.add("Pencil")
        test_object.add("Pen")
        prev_items = test_object.items()

        result = test_object.remove("Pencil")
        new_items = test_object.items()

        self.assertTrue(result)
        self.assertNotEqual(prev_items, new_items)  
        

    def test_remove_decrements_count(self):
        test_object:Backpack = Backpack("Lauren", 2)
        test_object.add("Pencil")
        test_object.add("Pen")
        prev_count = test_object.count()

        result = test_object.remove("Pencil")
        new_count = test_object.count

        self.assertTrue(result)
        self.assertGreater(prev_count, new_count)    

    def test_remove_missing_item(self):
        test_object:Backpack = Backpack("Lauren", 2)
        test_object.add("Pencil")
        test_object.add("Pen")
        prev_count = test_object.count()

        result = test_object.remove("Water Bottle")
        new_count = test_object.count

        self.assertFalse(result)
        self.assertEqual(prev_count, new_count)

    def test_allows_duplicate_items(self):
        test_object:Backpack = Backpack("Lauren", 3)
        test_object.add("Pencil")
        result = test_object.add("Pencil")

        self.assertTrue(result)

    def test_remove_one_duplicate_item(self):
        test_object:Backpack = Backpack("Lauren", 3)
        test_object.add("Pencil")
        test_object.add("Pencil")

        result = test_object.remove("Pencil")
        new_items = test_object.items()

        self.assertTrue(result)
        self.assertEqual("[Pencil]", new_items)

    def test_is_full_changes(self):
        test_object:Backpack = Backpack("Lauren", 1)
        prev_is_full = test_object.is_full()

        test_object.add("Pencil")
        new_is_full = test_object.is_full()

        self.assertFalse(prev_is_full)
        self.assertTrue(new_is_full)

    def test_items_returns_copy(self):
        test_object:Backpack = Backpack("Lauren", 2)
        test_object.add("Pencil")
        test_object.add("Pen")

        items = test_object.items()
        items.pop(0)

        test.assertNotEqual(test_object.items(), items)

    def test_str_is_correct_empty(self):
        test_object:Backpack = Backpack("Lauren", 5)
        test.assertEqual("Backpack(owner=Lauren, items=empty", str(test_object))

    def test_str_is_correct_full(self):
        test_object:Backpack = Backpck("Lauren", 3)
        test_object.add("Pencil")
        test_object.add("Pen")
        test_object.add("Water")

        test.assertEqual("Backpack(owner=Lauren, items=3/3)", str(test_object))


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