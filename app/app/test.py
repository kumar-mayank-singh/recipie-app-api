from django.test import TestCase
from app.calc import fun_add, sub


class Calculate(TestCase):
    
    def test_add_number(self):
        """Test that two numbers are added together"""
        self.assertEqual(fun_add(3,8),11)

    def test_sub_numbers(self):
        """Test that the values are subtracted and returned"""
        self.assertEqual(sub(5,11),6)