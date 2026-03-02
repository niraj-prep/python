temp =float(input("Enter temperature in degree Celsius: "))


if temp < -273.15:
	print("Invalid temperature: below absolute zero")
elif temp == -273.15:
	print("Temperature is absolute zero")
elif temp > -273.15 and temp < 0:
	print("Temperature is below freezing")
elif temp == 0:
	print("Temperature is at the freezing point")
elif temp < 100:
	print("Temperature is in the normal range")
elif temp == 100:
	print("Temperature is at the boiling point")
elif temp > 100:
	print("Temperature is above the boiling point")
else:
	print("Invalid entry")