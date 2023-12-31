#!/usr/bin/python3
"""Module that defines a class Student"""


class Student:
    """This Class represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dict representation of the Student"""
        return self.__dict__
