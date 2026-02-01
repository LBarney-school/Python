"""Tasks:

    Create a new file called manual_test_temp.py
    Import the functions from temperature_converter.py
    Write manual test cases using if/else to check expected results.
    Print "Test Passed" or "Test Failed" for each test.
    Answer the questions below directly into Blackboard.


Questions:

    What happens if you enter a float like 36.6 degrees Celsius?
    How can you add a test for negative temperatures?
    What would make these process difficult if the program had 100 functions?"""

import temperature_converter

# three tests for Fahrenheit to Celsius conversion
fahrenheit_test1_expected = 212
fahrenheit_test1_actual = temperature_converter.celsius_to_fahrenheit(100)
if fahrenheit_test1_actual == fahrenheit_test1_expected:
    print("Fahrenheit Conversion Test 1 Passed")
else:
    print("Fahrenheit Conversion Test 1 Failed")
    print(
        f"Expected value: {fahrenheit_test1_expected}, Actual value: {fahrenheit_test1_actual}"
    )


fahrenheit_test2_expected = 122
fahrenheit_test2_actual = temperature_converter.celsius_to_fahrenheit(50)
if fahrenheit_test2_actual == fahrenheit_test2_expected:
    print("Fahrenheit Conversion Test 2 Passed")
else:
    print("Fahrenheit Conversion Test 2 Failed")
    print(
        f"Expected value: {fahrenheit_test2_expected}, Actual value: {fahrenheit_test2_actual}"
    )

fahrenheit_test3_expected = 97.88
fahrenheit_test3_actual = temperature_converter.celsius_to_fahrenheit(36.6)
if fahrenheit_test3_actual == fahrenheit_test3_expected:
    print("Fahrenheit Conversion Test 3 Passed")
else:
    print("Fahrenheit Conversion Test 3 Failed")
    print(
        f"Expected value: {fahrenheit_test3_expected}, Actual value: {fahrenheit_test3_actual}"
    )

# three tests for Celsius to Fahrenheit to Celsius conversion
celsius_test1_expected = 37.77778
celsius_test1_actual = temperature_converter.fahrenheit_to_celsius(100)
if celsius_test1_actual == celsius_test1_expected:
    print("Celsius Conversion Test 1 Passed")
else:
    print("Celsius Conversion Test 1 Failed")
    print(
        f"Expected value: {celsius_test1_expected}, Actual value: {celsius_test1_actual}"
    )

celsius_test2_expected = 10
celsius_test2_actual = temperature_converter.fahrenheit_to_celsius(50)
if celsius_test2_actual == celsius_test2_expected:
    print("Celsius Conversion Test 2 Passed")
else:
    print("Celsius Conversion Test 2 Failed")
    print(
        f"Expected value: {celsius_test2_expected}, Actual value: {celsius_test2_actual}"
    )

celsius_test3_expected = -40
celsius_test3_actual = temperature_converter.fahrenheit_to_celsius(-40)
if celsius_test3_actual == celsius_test3_expected:
    print("Celsius Conversion Test 3 Passed")
else:
    print("Celsius Conversion Test 3 Failed")
    print(
        f"Expected value: {celsius_test3_expected}, Actual value: {celsius_test3_actual}`"
    )
