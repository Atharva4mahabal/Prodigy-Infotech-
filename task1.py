#Farenheit to Celsius

fahrenheit = float(input("Enter temperature in fahrenheit: "))

celsius = (fahrenheit - 32)/1.8

print(str(fahrenheit )+ " degree Fahrenheit is equal\
to " + str(celsius ) + " degree Celsius." )

#Celsius to Farenheit

# Temperature in celsius degree
celsius = 47

# Converting the temperature to
# fehrenheit using the formula
fahrenheit = (celsius * 1.8) + 32

# printing the result
print('%.2f Celsius is equivalent to: %.2f Fahrenheit'
	% (celsius, fahrenheit))

