shoplist = ["apple", "mango", "carrot", "banana"]

print("I have", len(shoplist), "item")

print("They are:",)

for item in shoplist:
	print(item,)

shoplist.append("rice")
print("\nadd rice,now is",)

for item in shoplist:
	print(item, end=' ')  #不换行

shoplist.sort()
print("\nSort have done,now is",)

for item in shoplist:
	print(item, end=' ')
olditem = shoplist[0]
del shoplist[0]
print("\nI bought", olditem)

print("now is", shoplist)
#元组打印
print("now is %s,%s,%s,%s"%(shoplist[0], shoplist[1], shoplist[2], shoplist[3]))

print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

