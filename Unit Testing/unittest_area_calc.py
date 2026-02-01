import unittest

import area_calc


# Unit testing for area calculator
class Test(unittest.TestCase):
    # test for triangle area
    def test_area_triangle(self):
        self.assertEqual(area_calc.area_triangle(10, 40), 200)
        self.assertEqual(area_calc.area_triangle(4, 8), 16)
        self.assertEqual(area_calc.area_triangle(7, 12), 42)

    # Test for rectangle area
    def test_area_rectangle(self):
        self.assertEqual(area_calc.area_rectangle(10, 40), 400)
        self.assertEqual(area_calc.area_rectangle(4, 8), 32)
        self.assertEqual(area_calc.area_rectangle(7, 12), 84)

    # Test for Circle Area
    def test_area_circle(self):
        self.assertAlmostEqual(area_calc.area_circle(10), 62.8)
        self.assertAlmostEqual(area_calc.area_circle(4), 25.12)
        self.assertAlmostEqual(area_calc.area_circle(7), 43.96)


if __name__ == "__main__":
    unittest.main()
