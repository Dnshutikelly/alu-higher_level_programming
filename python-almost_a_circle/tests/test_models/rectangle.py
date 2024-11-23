#!/usr/bin/python3
"""Test Rectangle"""

import unittest
from io import StringIO
from unittest.mock import patch
import os

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for rectangle"""

    def test_instance(self):
        """Test instance creation and input validation for Rectangle"""
        Base._Base__nb_objects = 0

        # Test instances of Rectangle with valid arguments
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r4.id, 5)  # Check that the id is correctly assigned

        # Test validation of width and height
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

        # Test validation for x and y
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

        # Test type validation for width, height, x, and y
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
        
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
        
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
        
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")
        
        # Test too many arguments
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5)

