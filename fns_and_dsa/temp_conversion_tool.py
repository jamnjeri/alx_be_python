# Define Global Conversion Factors:
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Write a function convert_to_celsius(fahrenheit) that takes a temperature in Fahrenheit and returns the temperature converted to Celsius.
def convert_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

# Write a function convert_to_fahrenheit(celsius) that takes a temperature in Celsius and returns the temperature converted to Fahrenheit.
def convert_to_fahrenheit(celsius):
  celsius = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return celsius

def main():
  try:
    # Prompt the user to enter a temperature and specify whether it’s in Celsius or Fahrenheit.
    temperature = float(input("Enter the temperature to convert: "))
    type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
  
    if type == 'F':
      result = convert_to_celsius(temperature)
      print(f"{temperature}°F is {result}°C")
    elif type == 'C':
      result = convert_to_fahrenheit(temperature)
      print(f"{temperature}°C is {result}°F")
    else:
      print("Invalid choice entered")
  except ValueError:
    print(f"Error: {e}. Please enter a numeric value for the temperature and 'C' or 'F' for the unit.")

if __name__ == "__main__":
    main()

