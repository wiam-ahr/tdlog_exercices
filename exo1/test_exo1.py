import unittest

from exo1 import Item


class Exo1Test(unittest.TestCase):

    def test_item_construction(self):
        item = Item(10, 20)

        self.assertEqual(20, item.weight)

# test_exo1.py
import unittest
from exo1 import Item

class Exo1Test(unittest.TestCase):

    def test_item_construction(self):
        item = Item(10, 20)
        self.assertEqual(item.price, 10)
        self.assertEqual(item.weight, 20)

if __name__ == '__main__':
    unittest.main()
