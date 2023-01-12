def celsius_to_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

# get user input
celsius = float(input("Enter temperature in celsius: "))

#conversion
fahrenheit = (celsius * 1.8) + 32

# Print result
print(str(celsius) + " degrees Celsius is equal to " + str(fahrenheit) + " degrees Farenheit.")
