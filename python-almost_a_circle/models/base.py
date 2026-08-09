#!/usr/bin/python3
"""Defines the Base class used as the parent of every model in this
project. It manages the id attribute so subclasses don't have to
duplicate that logic, and provides shared JSON/CSV serialization
helpers.
"""
import json
import csv
import turtle


class Base:
    """Base class managing the id attribute for all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as jsonfile:
            jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string (str): A JSON string representing a list of
                dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            **dictionary (dict): Key/value pairs of attributes to
                initialize the new instance with.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class name>.json."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of list_objs to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            list_objs = []
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            else:
                fields = ["id", "size", "x", "y"]
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                writer.writerow([obj_dict[field] for field in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from <Class name>.csv."""
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                list_dicts = [
                    {field: int(value) for field, value in zip(fields, row)}
                    for row in reader
                ]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw every Rectangle and Square.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        colors = ["#ecf0f1", "#f1c40f", "#2ecc71", "#3498db",
                  "#9b59b6", "#e67e22"]

        all_shapes = list(list_rectangles) + list(list_squares)
        for index, shape in enumerate(all_shapes):
            turt.color(colors[index % len(colors)])
            turt.showturtle()
            turt.up()
            turt.goto(shape.x, shape.y)
            turt.down()
            for _ in range(2):
                turt.forward(shape.width)
                turt.left(90)
                turt.forward(shape.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
