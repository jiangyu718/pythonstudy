listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)

def powersum(power, *args):
	'''Return the sum of each argument raised to specified power.'''
	total = 0
	for i in args:
		total += pow(i, power)
	return total


exec('print(powersum(2,3,4))')
exec('print(powersum(2,10))')

eval('2+3*3')  #去掉字符串的引号

mylist = ['item']
assert len(mylist) >= 1
mylist.pop()
#assert len(mylist) >= 1


i=[]
i.append('item')
print(i)
print(repr(i))
print(2*3)