import sys
import test1
print("The command and line arguments are")

for i in sys.argv:
	print(i)

print("\nThe python path is ", sys.path,"\n")

if __name__ == "__main__":
	print("This program is being run by itself")
else:
	print("I am being imported from another module")

#调用模块就是说import那个文件的除.py的名字，然后用这个名字.函数，来调用其中的函数
test1.printMax(1,2)
