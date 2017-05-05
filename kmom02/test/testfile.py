"""
A testfile to test car.py
"""

import unittest
import car

class Testcase(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    bmw = car.Car("BMW", 100000)
    volvo = car.Car("Volvo", 150000)
    
    # Name the function test_ to allow verbose information.
    def test_if_objects_are_same(self):
        """ Returns True if instances are not same """
        self.assertIsNot(self.bmw, self.volvo)

    def test_attribute(self):
        """ Returns True attribute matches expected """
        self.assertIs(self.bmw.model, "BMW")
        self.assertIs(self.volvo.model, "Volvo")

    def test_sum_instances(self):
        """ Returns True if __add__ is correct """
        self.assertEqual(self.volvo + self.bmw, 250000)

    def test_equipment(self):
        """ Returns True if Airbag exists in equipment """

        self.bmw.addEquipment("Bluetooth")
        self.bmw.addEquipment("Airbag")
        self.bmw.addEquipment("AC")

        self.assertIn("Airbag", self.bmw.equipment)


if __name__ == '__main__':
    unittest.main()
