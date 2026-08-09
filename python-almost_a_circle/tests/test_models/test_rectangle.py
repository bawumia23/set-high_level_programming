#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    # -- instantiation ----------------------------------------------

    def test_is_base(self):
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Base)

    def test_two_args(self):
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 0, 0))

    def test_three_args(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 0))

    def test_four_args(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_five_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (5, 1, 2, 3, 4))

    # -- TypeError validation ----------------------------------------

    def test_width_str_type_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle("1", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_height_str_type_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_x_str_type_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, "3")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_y_str_type_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_width_dict_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2)
            r.x = {}

    # -- ValueError validation ----------------------------------------

    def test_width_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(-1, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_width_zero_value_error(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_zero_value_error(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, -3)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 3, -4)
        self.assertEqual(str(e.exception), "y must be >= 0")

    # -- area / __str__ / display --------------------------------------

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_without_x_and_y(self):
        r = Rectangle(2, 2)
        expected = "##\n##\n"
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), expected)

    def test_display_without_y(self):
        r = Rectangle(3, 2, 1)
        expected = " ###\n ###\n"
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), expected)

    def test_display_with_x_and_y(self):
        r = Rectangle(2, 3, 2, 2)
        expected = "\n\n  ##\n  ##\n  ##\n"
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), expected)

    # -- to_dictionary --------------------------------------------------

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_to_dictionary_roundtrip(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))

    # -- update (*args) ---------------------------------------------------

    def test_update_no_args(self):
        r = Rectangle(1, 2)
        original = str(r)
        r.update()
        self.assertEqual(str(r), original)

    def test_update_1_arg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_2_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_3_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_4_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_5_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 1, 2, 3, 4))

    # -- update (**kwargs) -----------------------------------------------

    def test_update_kwargs_id(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(**{"id": 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(**{"id": 89, "width": 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_kwargs_id_width_height(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_kwargs_id_width_height_x(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(**{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_kwargs_id_width_height_x_y(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 1, 2, 3, 4))

    # -- Base.create -------------------------------------------------------

    def test_create_id_only(self):
        r = Rectangle.create(**{"id": 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        r = Rectangle.create(**{"id": 89, "width": 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_create_id_width_height(self):
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_create_id_width_height_x(self):
        r = Rectangle.create(
            **{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_create_id_width_height_x_y(self):
        r = Rectangle.create(
            **{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 1, 2, 3, 4))

    def test_create_roundtrip(self):
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)
        self.assertEqual(str(r1), str(r2))

    # -- save_to_file / load_from_file --------------------------------

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_one_instance(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn('"width": 1', content)
        self.assertIn('"height": 2', content)
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exists(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_output = Rectangle.load_from_file()
        self.assertEqual(len(list_output), 2)
        self.assertEqual(str(list_output[0]), str(r1))
        self.assertEqual(str(list_output[1]), str(r2))
        os.remove("Rectangle.json")

    # -- save_to_file_csv / load_from_file_csv --------------------------

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
