shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist

del shoplist[0]
print(shoplist)
print(mylist)

mylist = shoplist[:]
print(mylist)