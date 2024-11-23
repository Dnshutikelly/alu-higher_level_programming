#!/usr/bin/python3
"""Test for Square"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test for class Square"""

    def test_instance(self):
        """Test instances of Square with different arguments"""
        s1 = Square(1)  # Basic initialization
        s2 = Square(1, 2)  # With 'x'
        s3 = Square(1, 2, 3)  # With 'x' and 'y'
        s4 = Square(1, 0)  # 'x' as 0
        s5 = Square(1, 2, 3, 4)  # With 'x', 'y', and custom ID

        self.assertEqual(s1.id, 1)  # Ensure ID is assigned correctly
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 3)
        self.assertEqual(s4.id, 4)
        self.assertEqual(s5.id, 5)  # Verify the incremented IDs

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s6 = Square(-1, 2)  # Invalid width

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s7 = Square(1, -2)  # Invalid 'x'

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s8 = Square(0, 2)  # Zero width

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s9 = Square(1, 2, -3)  # Invalid 'y'

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s10 = Square(0)  # Zero width

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s11 = Square("1")  # Invalid width type

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s12 = Square(1, "2")  # Invalid 'x' type

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s13 = Square(1, 2, "3")  # Invalid 'y' type

    def test_area(self):
        """Test area method of Square"""
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)  # Area should be width * width
        s2 = Square(3)
        self.assertEqual(s2.area(), 9)  # Area should be 3*3 = 9

    def test_str(self):
        """Test string representation of Square"""
        s1 = Square(2, 1, 1, 1)
        self.assertEqual(str(s1), "[Square] (1) 1/1 - 2")

    def test_to_dictionary(self):
        """Test to_dictionary method of Square"""
        s1 = Square(2, 1, 1, 1)
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'size': 2, 'x': 1, 'y': 1})

    def test_update(self):
        """Test update method of Square"""
        s1 = Square(2, 1, 1, 1)
        s1.update(10, 3, 2, 1)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 1)

    def test_create(self):
        """Test create method of Square"""
        s1 = Square.create(id=5, size=3, x=2, y=1)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 1)

    def test_save_to_file(self):
        """Test save_to_file method of Square"""
        Square.save_to_file([Square(2)])
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertTrue("id" in content)
            self.assertTrue("size" in content)
        os.remove("Square.json")  # Clean up file

    def test_load_from_file(self):
        """Test load_from_file method of Square"""
        Square.save_to_file([Square(2)])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertEqual(squares[0].size, 2)
        os.remove("Square.json")  # Clean up file

if __name__ == '__main__':
    unittest.main()

