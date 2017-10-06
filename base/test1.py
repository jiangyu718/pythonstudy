def printMax(x, y):
	'''Print max num
	the two values must be integers.'''
	x = int(x);
	y = int(y);

	if x > y:
		print(x, "is maximum")
	else:
		print(y, "is maximum")

printMax(3, 5)
help(printMax)
print(printMax.__doc__)