#!/usr/bin/python3
"""
This module comprises a Base class.
"""

import json
import csv
import turtle


class Base:
    """My Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string - encode object into a JSON string respresentation.
        args:
        - list_dictionaries: a list of dictionaries.
        Return:
        The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - writes the JSON string representation
                    of list_objs to a file.
        args:
        - cls: class.
        - list_objs:  a list of instances who inherits of Base
                    example: list of Rectangle or list of Square instances.
        """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        """Convert list of objects into list of dictionaries"""
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        """list_dicts = [cls.to_dictionary(obj) for obj in list_objs]"""
        """convert list of dictionaries to JSON string"""
        json_str = cls.to_json_string(list_dicts)

        """Write JSON string to file, overwriting if it already exists"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string - deserialize json string.
        args:
        - json_string: a string representing a list of dictionaries.
        Return:
        If json_string is None or empty, return an empty list.
        Otherwise, return the list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """"returns an instance with all attributes already set"""
        dummy_objs = cls(1, 1)
        cls.update(dummy_objs, **dictionary)

        return dummy_objs

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="utf-8") as file:
                json_str = file.read()
        except FileNotFoundError:
            return []

        list_dict = cls.from_json_string(json_str)

        instances = [cls.create(**obj_dict) for obj_dict in list_dict]

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize python object to csv."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from CSV file."""
        filename = cls.__name__ + ".csv"
        objs = []
        with open(filename, newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                objs.append(cls.from_csv_row(row))
                return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws all rectangles and squares using Turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle objects to draw.
            list_squares (list): List of Square objects to draw.
        """
        # Create a screen for drawing
        screen = turtle.Screen()
        screen.title("Rectangles and Squares")

        # Set up the turtle
        t = turtle.Turtle()
        t.speed(0)  # Set the drawing speed (0 is fastest)
        t.penup()   # Lift the pen (don't draw while moving)
        t.hideturtle()  # Hide the turtle icon

        # Draw rectangles
        for rect in list_rectangles:
            t.setpos(rect.x, rect.y)  # Move turtle to the starting position of the rectangle
            t.pendown()  # Lower the pen (start drawing)
            t.begin_fill()  # Begin filling the shape
            t.color("blue")  # Set the color of the shape (example color: blue)
            for _ in range(2):
                t.forward(rect.width)  # Move forward by the width of the rectangle
                t.left(90)  # Turn left by 90 degrees (to draw a corner)
                t.forward(rect.height)  # Move forward by the height of the rectangle
                t.left(90)  # Turn left by 90 degrees (to draw another corner)
            t.end_fill()  # End filling the shape
            t.penup()  # Lift the pen (stop drawing)

        # Draw squares
        for square in list_squares:
            t.setpos(square.x, square.y)  # Move turtle to the starting position of the square
            t.pendown()  # Lower the pen (start drawing)
            t.begin_fill()  # Begin filling the shape
            t.color("green")  # Set the color of the shape (example color: green)
            for _ in range(4):
                t.forward(square.size)
                t.left(90)
            t.end_fill()
            t.penup()

        screen.exitonclick()
