#import _compat_pickle as p
import pickle as p

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
p.dump(shoplistfile, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')
storelist = p.load(f)
print(storelist)

