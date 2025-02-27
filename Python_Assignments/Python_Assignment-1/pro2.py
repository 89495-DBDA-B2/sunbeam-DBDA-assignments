# 2] Write a Python Program to Convert Celsius To Fahrenheit vice versa.
#    fahrenheit = (celsius * 1.8) + 32


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

print("Temperature Conversion: Celsius to Fahrenheit")

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")