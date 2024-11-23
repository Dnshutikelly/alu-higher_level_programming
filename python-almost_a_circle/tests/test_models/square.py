import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_square_creation(self):
        s = Square(5, 1, 1, 12)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.id, 12)

    def test_update_square(self):
        s = Square(5, 1, 1, 12)
        s.update(10)
        self.assertEqual(s.size, 10)
        s.update(15, 2, 2, 20)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 20)

    def test_to_dictionary(self):
        s = Square(5, 1, 1, 12)
        self.assertEqual(s.to_dictionary(), {'id': 12, 'size': 5, 'x': 1, 'y': 1})

if __name__ == '__main__':
    unittest.main()

