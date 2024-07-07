FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

tmp = float(input('Enter the temperature to convert: '))
temp_type = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').lower()

def convert_to_celsius(tmp):
        return (tmp-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(tmp):
       return (tmp*CELSIUS_TO_FAHRENHEIT_FACTOR)+32

celcius = convert_to_celsius(tmp)
faren = convert_to_fahrenheit(tmp)

if temp_type == 'f':
    print(f"{temp}ºF is {celcius}ºC")
elif temp_type == 'c':
    print(f"{temp}ºC is {faren}ºF")
else:
    print("Invalid temperature. Please enter a numeric value.")

