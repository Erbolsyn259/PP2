def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = fahrenheit_to_celsius(fahrenheit)
print(f"The temperature in Celsius is: {celsius}")
