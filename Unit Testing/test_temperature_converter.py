import unittest

import temperature_converter


# unit testing for Temperature Converter Class
class TestTemperatureConverter(unittest.TestCase):

    # Testing function for Celsius to Fahrenheit function
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(temperature_converter.celsius_to_fahrenheit(270), 518)
        self.assertEqual(temperature_converter.celsius_to_fahrenheit(100), 212)
        self.assertEqual(temperature_converter.celsius_to_fahrenheit(-100), -148)

    # Testing function for Fahrenheit to Celsius function
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(temperature_converter.fahrenheit_to_celsius(32), 0)
        self.assertEqual(temperature_converter.fahrenheit_to_celsius(50), 10)
        self.assertEqual(temperature_converter.fahrenheit_to_celsius(212), 100)


if __name__ == "__main__":
    unittest.main()
