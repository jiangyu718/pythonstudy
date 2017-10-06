def sayjy():
	print("jy")
	print("yj")
	print("jjyy")


def sayjyab(a, b):
	if a == 2:
		print("jy")
	print("yj")
	print("jjyy")


num = 23
#guess = int(input('Enter an integer:'))
guess = 23
if guess == num:
	print("guess == num")
	print("guess == num too")
elif guess < num:
	print("<")
else:
	print(">")
print ('Done')

running = True
while running:
	print ("Yes")
	running = False

for i in range(1,5):
	#print(i)
	if i == 3:
		print("now", i)
	else:
		print(i)
	continue
else:
	print("stop in", i)

sayjy()
sayjyab(b=2, a=3)

print("")
