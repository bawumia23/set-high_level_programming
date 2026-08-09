#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_public(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none_autoincrement(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_zero(self):
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_none_type(self):
        b = Base()
        self.assertIsInstance(b.id, int)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        list_dicts = [{"id": 1, "width": 10, "height": 2, "x": 0, "y": 0}]
        result = Base.to_json_string(list_dicts)
        self.assertIsInstance(result, str)
        self.assertEqual(Base.from_json_string(result), list_dicts)

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)
        self.assertEqual(str(r1), str(r2))

    def test_create_square(self):
        s1 = Square(5, 1, 2, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)
        self.assertEqual(str(s1), str(s2))

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_and_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_output = Rectangle.load_from_file()
        self.assertEqual(len(list_output), 2)
        self.assertEqual(str(list_output[0]), str(r1))
        self.assertEqual(str(list_output[1]), str(r2))
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_save_and_load_from_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        list_output = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_output), 2)
        self.assertEqual(str(list_output[0]), str(r1))
        self.assertEqual(str(list_output[1]), str(r2))
        os.remove("Rectangle.csv")

    def test_load_from_file_csv_no_file(self):
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        self.assertEqual(Rectangle.load_from_file_csv(), [])


if __name__ == "__main__":
    unittest.main()
