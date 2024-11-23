#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines the blueprint for a Square object"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Returns the size [width/height] of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size [width/height] of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values of Square object attributes"""
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i == 0 and arg is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id" and value is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    if key in attributes:
                        setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square object"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

