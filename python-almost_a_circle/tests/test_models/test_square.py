#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
import os
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    # -- instantiation ----------------------------------------------

    def test_is_rectangle(self):
        s = Square(1)
        self.assertIsInstance(s, Rectangle)

    def test_one_arg(self):
        s = Square(1)
        self.assertEqual((s.size, s.x, s.y), (1, 0, 0))

    def test_two_args(self):
        s = Square(1, 2)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 0))

    def test_three_args(self):
        s = Square(1, 2, 3)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 3))

    def test_four_args(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (4, 1, 2, 3))

    # -- TypeError validation ----------------------------------------

    def test_size_str_type_error(self):
        with self.assertRaises(TypeError) as e:
            Square("1")
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_x_str_type_error(self):
        with self.assertRaises(TypeError) as e:
            Square(1, "2")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_y_str_type_error(self):
        with self.assertRaises(TypeError) as e:
            Square(1, 2, "3")
        self.assertEqual(str(e.exception), "y must be an integer")

    # -- ValueError validation ----------------------------------------

    def test_size_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            Square(-1)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_x_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            Square(1, -2)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            Square(1, 2, -3)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_size_zero_value_error(self):
        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")

    # -- area / __str__ ------------------------------------------------

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    # -- size property ----------------------------------------------------

    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_type_error(self):
        s = Square(5)
        with self.assertRaises(TypeError) as e:
            s.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

    # -- to_dictionary --------------------------------------------------

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_to_dictionary_roundtrip(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))

    # -- update (*args) ---------------------------------------------------

    def test_update_no_args(self):
        s = Square(5)
        original = str(s)
        s.update()
        self.assertEqual(str(s), original)

    def test_update_1_arg(self):
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_2_args(self):
        s = Square(5)
        s.update(89, 1)
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_3_args(self):
        s = Square(5)
        s.update(89, 1, 2)
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_4_args(self):
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    # -- update (**kwargs) -----------------------------------------------

    def test_update_kwargs_id(self):
        s = Square(5)
        s.update(**{"id": 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        s = Square(5)
        s.update(**{"id": 89, "size": 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_kwargs_id_size_x(self):
        s = Square(5)
        s.update(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_kwargs_id_size_x_y(self):
        s = Square(5)
        s.update(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    # -- Base.create -------------------------------------------------------

    def test_create_id_only(self):
        s = Square.create(**{"id": 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        s = Square.create(**{"id": 89, "size": 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_create_id_size_x(self):
        s = Square.create(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_create_id_size_x_y(self):
        s = Square.create(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_create_roundtrip(self):
        s1 = Square(5, 1, 2, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsNot(s1, s2)
        self.assertEqual(str(s1), str(s2))

    # -- save_to_file / load_from_file --------------------------------

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_one_instance(self):
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertIn('"size": 1', content)
        os.remove("Square.json")

    def test_load_from_file_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        list_output = Square.load_from_file()
        self.assertEqual(len(list_output), 2)
        self.assertEqual(str(list_output[0]), str(s1))
        self.assertEqual(str(list_output[1]), str(s2))
        os.remove("Square.json")

    # -- save_to_file_csv / load_from_file_csv --------------------------

    def test_save_and_load_from_file_csv(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file_csv([s1, s2])
        list_output = Square.load_from_file_csv()
        self.assertEqual(len(list_output), 2)
        self.assertEqual(str(list_output[0]), str(s1))
        self.assertEqual(str(list_output[1]), str(s2))
        os.remove("Square.csv")

    def test_load_from_file_csv_no_file(self):
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")
        self.assertEqual(Square.load_from_file_csv(), [])


if __name__ == "__main__":
    unittest.main()
