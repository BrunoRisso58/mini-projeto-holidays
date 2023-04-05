from django.test import TestCase
import unittest
from views import isHoliday


class TestHolidayViews(unittest.TestCase):
    def test_isHoliday(self):
        self.assertEqual(isHoliday("2023-01-01"), "um dia comum ou outro feriado")
        self.assertEqual(isHoliday("2023-04-21"), "Tiradentes")
        self.assertEqual(isHoliday("2023-12-25"), "Natal")