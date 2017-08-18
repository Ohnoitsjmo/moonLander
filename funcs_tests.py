# Project 2 - Moonlander
#
# Name: Justin Mo
# Instructor: Brian Jones
# Section: 17

import unittest
from lander_funcs import *

class TestCases(unittest.TestCase):
   def test_update_acc1(self):
      self.assertAlmostEqual(update_acceleration(1.62, 0), -1.62)
   def test_update_acc2(self):
      self.assertAlmostEqual(update_acceleration(1.62, 1), -1.296)
   
   def test_update_alt1(self):
      self.assertAlmostEqual(update_altitude(1, 2, 3), 4.5)
   def test_update_alt2(self):
      self.assertAlmostEqual(update_altitude(3, 2, 1), 5.5)   

   def test_update_vel1(self):
      self.assertAlmostEqual(update_velocity(5, 3), 8)
   def test_update_vel2(self):
      self.assertAlmostEqual(update_velocity(7, 4), 11)
  
   def test_update_fuel1(self):
      self.assertAlmostEqual(update_fuel(7, 3), 4)
   def test_update_fuel2(self):
      self.assertAlmostEqual(update_fuel(9, 6), 3)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

