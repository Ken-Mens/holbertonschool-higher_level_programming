#!/usr/bin/python3
"""Unittest for Base"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    @classmethod
    def setUp(self):
        Base._Base__nb_objects = 0
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base(11)
        cls.b4 = Base("eleven")
        cls.b5 = Base(2.2)
        cls.r1 = Rectangle(1, 4, 0, 6)
        cls.r2 = Rectangle(8, 9)

    @classmethod
    def tearDown(self):
        pass
