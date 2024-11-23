#!/usr/bin/python3
"""
Write the class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle object."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the value for width"""
        return self.__width

    @property
    def height(self):
        """Gets the value for height"""
        return self.__height

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x

    @property
    def y(self):
        """Gets the value for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the value for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the value for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """Return the string representation of the rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates the values of Rectangle attributes"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i == 0 and arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id" and value is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    if key in attributes:
                        setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

