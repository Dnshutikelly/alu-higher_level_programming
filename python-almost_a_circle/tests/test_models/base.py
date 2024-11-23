import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def test_id_assignment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_given(self):
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{"id": 12}])

    def test_save_to_file(self):
        b1 = Base(45)
        b1.save_to_file([b1])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 45}]')

    def test_load_from_file(self):
        b1 = Base(45)
        b1.save_to_file([b1])
        loaded = Base.load_from_file()
        self.assertEqual(loaded[0].id, 45)


if __name__ == '__main__':
    unittest.main()

