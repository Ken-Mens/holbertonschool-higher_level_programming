#!/usr/bin/python3
"""Unittest for Base"""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for base"""
    @classmethod
    def setUp(cls):
        Base._Base__nb_objects = 0
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base(11)
        cls.b4 = Base("eleven")
        cls.b5 = Base(4.4)
        cls.r1 = Rectangle(1, 4, 0, 6)
        cls.r2 = Rectangle(8, 9)

    def test_true(self):
        """Tests the creation of a Base"""
        self.assertTrue(self.b1)

    def test_id(self):
        """ test id attribute """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 11)
        self.assertEqual(self.b4.id, "eleven")
        self.assertEqual(self.b5.id, 4.4)

    def test_16_0_saveToFile(self):
        """Checks to make sure file created and written"""
        Rectangle.save_to_file([self.r1, self.r2])
        self.assertTrue(os.path.isfile("Rectangle.json"))

    @classmethod
    def tearDown(self):
        pass
