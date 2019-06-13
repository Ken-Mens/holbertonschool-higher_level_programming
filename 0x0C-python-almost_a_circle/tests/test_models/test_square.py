#!/usr/bin/python3
import unittest
import json
import io
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Class runs multiple tests Square"""
    @classmethod
    def setUp(self):
        """sets up instances"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(9)
        cls.s2 = Square(7, 8)
        cls.s3 = Square(8, 3, 4)
        cls.s4 = Square(4, 1, 2, 9)

    def test_create(self):
        """Checks if the creation was successful"""
        self.assertTrue(self.s1)
        self.assertTrue(self.s2)
        self.assertTrue(self.s3)
        self.assertTrue(self.s4)

    def test_area(self):
        """Test area()"""
        self.assertEqual(self.s1.area(), 81)
        self.assertEqual(self.s2.area(), 49)
        self.assertEqual(self.s3.area(), 64)
        self.assertEqual(self.s4.area(), 16)

    def test_size(self):
        """ test size """
        self.assertEqual(self.s1.size, 9)
        self.assertEqual(self.s2.size, 7)
        self.assertEqual(self.s3.size, 8)
        self.assertEqual(self.s4.size, 4)

    def test_x(self):
        """ test x """
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 8)
        self.assertEqual(self.s3.x, 3)
        self.assertEqual(self.s4.x, 1)

    def test_y(self):
        """ test y """
        self.assertEqual(self.s1.y, 4)
        self.assertEqual(self.s2.y, 9)
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.y, 1)

    def test_id(self):
        """ test id """
        self.assertEqual(self.s1.id, 8)
        self.assertEqual(self.s2.id, 6)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 5)

    def test_init_negative_size(self):
        """Initialize with negative value"""
        with self.assertRaises(ValueError) as v:
            Square(4, -6)
            self.assertEqual(str(v.exception), "width must be >= 0")

    def test_str(self):
        """Testing the __str__ """
        self.assertEqual(Square.__str__
                         (self.s1), "[Square] (11) 0/0 - 9")
        self.assertEqual(Square.__str__
                         (self.s2), "[Square] (12) 0/0 - 8")
        self.assertEqual(Square.__str__
                         (self.s3), "[Square] (13) 2/0 - 7")
        self.assertEqual(Square.__str__
                         (self.s4), "[Square] (14) 1/2 - 4")

    @classmethod
    def tearDown(self):
        """clears the board """
        pass
