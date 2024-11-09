#!/usr/bin/python3
"""
A class that inherits from list and adds a method to print the list sorted.
"""

class MyList(list):
    """Class MyList that extends list and adds a print_sorted method."""
    
    def __str__(self):
        """Return the string representation of the list."""
        return super().__str__()

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))  # Using sorted() to print a new sorted list
