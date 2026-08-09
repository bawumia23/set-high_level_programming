#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_is_base(self):
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Base)

    def test_width_height_x_y(self):
        r = Rectangle(10, 2, 1, 9, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 9)
        self.assertEqual(r.id, 5)

    def test_default_x_y(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_width_type_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_width_value_error(self):
        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_x_type_error(self):
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_y_value_error(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        r = Rectangle(2, 2)
        expected = "##\n##\n"
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), expected)

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_to_dictionary_roundtrip(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
