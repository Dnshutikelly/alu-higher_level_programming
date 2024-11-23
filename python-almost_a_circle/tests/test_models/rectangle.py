import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def test_rectangle_creation(self):
        r = Rectangle(10, 5, 1, 1, 99)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 99)

    def test_rectangle_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(-1, 5)
        with self.assertRaises(TypeError):
            Rectangle("str", 5)

    def test_rectangle_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, -1)
        with self.assertRaises(TypeError):
            Rectangle(10, "str")

    def test_rectangle_invalid_x(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -1, 1)

    def test_rectangle_invalid_y(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 5, 1, -1)

    def test_area(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(4, 3, 1, 1)
        with self.assertLogs() as log:
            r.display()
        expected_output = "\n\n####\n####\n####\n"
        self.assertEqual(log.output[0], expected_output)

    def test_str(self):
        r = Rectangle(4, 3, 1, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 1/1 - 4/3")

    def test_update(self):
        r = Rectangle(10, 5, 1, 1, 99)
        r.update(10)
        self.assertEqual(r.width, 10)
        r.update(15, 10, 5, 2, 3)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 2)

    def test_to_dictionary(self):
        r = Rectangle(4, 6, 2, 3, 12)
        self.assertEqual(r.to_dictionary(), {'id': 12, 'width': 4, 'height': 6, 'x': 2, 'y': 3})

    def test_save_to_file(self):
        r = Rectangle(10, 5, 1, 1, 99)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 99, "width": 10, "height": 5, "x": 1, "y": 1}]')

    def test_load_from_file(self):
        r = Rectangle(10, 5, 1, 1, 99)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(loaded[0].id, 99)
        self.assertEqual(loaded[0].width, 10)

if __name__ == '__main__':
    unittest.main()

