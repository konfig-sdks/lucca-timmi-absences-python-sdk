# coding: utf-8

"""
    Timmi Absences API

    Welcome on the documentation for Timmi Absences API.

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

import unittest

import os
from pprint import pprint
from lucca_timmi_absences_python_sdk import LuccaTimmiAbsences

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        luccatimmiabsences = LuccaTimmiAbsences(
        
                        authorization = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(luccatimmiabsences)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
