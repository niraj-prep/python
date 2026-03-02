num = int(input("Enter a positive integer: "))

if num < 1:
	print("Please enter a number greater than 0")
else:
	sum = 0
	for i in range(1,num+1):
		sum = sum + i
	print("The sum of numbers from 1 to %d is:"%(num),sum)