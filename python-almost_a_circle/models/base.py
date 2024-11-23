#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in the project.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dicts.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of objects to a file.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of objects represented by a JSON string.
        """
        if json_string == "[]" or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a JSON file.
        """
        try:
            with open(cls.__name__ + ".json", "r") as jsonfile:
                obj_list = cls.from_json_string(jsonfile.read())
                return [cls(**obj) for obj in obj_list]
        except FileNotFoundError:
            return []

