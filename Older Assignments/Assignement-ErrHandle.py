'''A temperature converter that reads temperatures from a file and converts them from Celsius to Fahrenheit. It assumes the file exists and all data is correct.'''

def read_temperatures(file_path: str) -> list[float]:
    try:
        with open(file_path, "r") as file:
            try:
                return [float(line.strip()) for line in file.readlines()]
            except ValueError:
                # exception for non-numerical values
                print("Invalid input.")
    except FileNotFoundError:
        print("File not found.")

def convert_to_fahrenheit(celsius: float) -> float:
    try:
        return (celsius * 9 / 5) + 32
    except:
        #exception for non-numerical values
        return "Invalid input."


def convert_file_temperatures(file_path: str):
    temps = read_temperatures(file_path)
    for temp in temps:
        fahrenheit = convert_to_fahrenheit(temp)
        print(f"{temp:.2f}°C = {fahrenheit:.2f}°F")


def main():
    #main try except
    try:
        file_path = input("Enter the temperature file path: ")
        convert_file_temperatures(file_path)
    except:
        print("Error occured.")



main()