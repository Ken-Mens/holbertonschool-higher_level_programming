#!/usr/bin/python3
import unittest
import json
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Runs tests for rectangle"""

    @classmethod
    def setUpClass(cls):
        """Sets up the testing environment"""
        Base = _Base__nb_objects = 0
        cls.r1 = Rectangle(6, 6)
        cls.r2 = Rectangle(3, 3)
        cls.r3 = Rectangle(4, 6, 9)
        cls.r4 = Rectangle(7, 5, 3, 2, 8)

    def test_id(self):
        """ test id  """
        self.assertEqual(self.r1.id, 11)
        self.assertEqual(self.r2.id, 4)
        self.assertEqual(self.r3.id, 7)
        self.assertEqual(self.r4.id, 6)

    def test_width(self):
        """Testing width"""
        self.assertEqual(self.r1.width, 6)
        self.assertEqual(self.r2.width, 3)
        self.assertEqual(self.r3.width, 4)
        self.assertEqual(self.r4.width, 7)

    def test_height(self):
        """Tests when integers are added for width"""
        self.assertEqual(self.r1.height, 6)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r3.height, 6)
        self.assertEqual(self.r4.height, 5)

    def test_x(self):
        """Tests for x"""
        self.assertEqual(self.r1.x, 8)
        self.assertEqual(self.r2.x, 5)
        self.assertEqual(self.r3.x, 7)
        self.assertEqual(self.r4.x, 7)
        self.assertEqual(self.r5.x, 6)

    def test_y(self):
        """Tests for y"""
        self.assertEqual(self.r1.y, 9)
        self.assertEqual(self.r2.y, 8)
        self.assertEqual(self.r3.y, 5)
        self.assertEqual(self.r4.y, 2)
        self.assertEqual(self.r5.y, 7)

    def test_area(self):
        """ test area """
        self.assertEqual(self.r1.area(), 36)
        self.assertEqual(self.r2.area(), 9)
        self.assertEqual(self.r3.area(), 24)
        self.assertEqual(self.r4.area(), 35)

    def test_subclass(self):
        """Checks if Rectangle is a subclass"""
        self.assertTrue(issubclass(Rectangle, Base))

    @classmethod
    def tearDownClass(cls):
        """Clears the board"""
        pass
