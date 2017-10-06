import re
m = re.match('foo', 'foo')

if m is not None:
	print(m.group())

print(m)

m = re.match('foo', 'bar')
if m is not None:       #False
	print(m.group())

m = re.match('foo', 'asfood on the table')
if m is not None:
	print('@1')
	print(m.group())

m = re.search('foo', 'asfood on the table')
if m is not None:
	print('@2')
	print(m.group())

print("1 *************************")

anyend = r'(?s).end'

m = re.match(anyend, '\nend')
if m is not None: print(m.group())
#顺序是看左括号的
m = re.match('((\w)\w\w)-(\d\d)(\d)', 'abc-123')
print(m.group())    #group是直接输出的匹配结果
print(m.groups())   #groups是以元组的方式呈现子组
print(m.group(1))
print(m.group(2))
print(m.group(3))

print("2 *************************")

m = re.match('((a)b),(ab)', 'ab,ab')
print(m.groups())

print("3 *************************")
print(bool(re.search('\W', '.')))
print('@1')
m = re.search(r'The\b', 'end. The')
if m is not None: print(m.group())
else: print('m is None')
print('@2')
m = re.search(r'\bThe', 'end The.end')
if m is not None: print(m.group())
else: print('m is None')

print("4 findall********************")

print(re.findall('car', 'carry the barcardi to the car'))

print("5 finditer********************")
s = 'This and that.'
ite = re.finditer(r'(th\w+) and (th\w+)', s, re.I)
#next(ite)
#for m in ite: print(m.groups())
g = re.finditer(r'(th\w+) and (th\w+)', s, re.I).__next__()
print(g.groups())

print("6 finditer*********************")
ite = re.finditer(r'(th\w+)', s, re.I)
#g = ite.__next__()
g = next(ite)
print(g.group())
g = next(ite)
print(g.group())

print("7 sub *********************") #替换
print(re.sub('X', 'Mr.Smith', r'attn:X\n\nDear X,\n'))
#会显示替换了几处
print(re.subn('X', 'Mr. Smith', r'attn: X\n\nDear X,\n'))

#利用group的\1 \2表示第几个子组
print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',\
        r'\2/\1/\3', '2/20/91'))

print("8 split *********************")
m = re.split(':', 'str1:str2:str3')
print(m)

DATA = (
	'Mountain View, CA 94040',
	'Sunnyvale, CA',
	'Los Altos, 94023',
	'Cupertino 95014',
	'Palo Alto CA',
	)
#DATA.__reversed__()
print(DATA)
for datum in DATA:
	m = re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum)
	print(m)

print("9  扩展符号 *********************")
m = re.findall(r'yes Yes', 'yes Yes yes yes')
print('@0')
print(m)
m = re.findall(r'(?i)yes', 'yes? Yes. YES!!')
print('@1')
print(m)
#['yes', 'Yes', 'YES']
m = re.findall(r'(?i)th\w+', 'The quickest way is through this\
		tunnel.')
print('@2')
print(m)
#

m = re.findall(r'(?im)^th[\w ]+', """
This line is the first,th
theanother line,
another line,
that line, it's the best
""")
print('@3')
print(m)

m = re.findall(r'th.+', '''
	The first line
    the second line
	the third line
	''')
print(m)

m = re.findall(r'(?s)th.+', '''
	The first line
	the second line
	the third line
	''')
print(m)

#re.X/VERBOSE
m = re.search(r'''(?x)
		\((\d{3})\)	#区号  
		[ ]			#空白符
		(\d{3})		#前缀
		-			#横线
		(\d{4})		#终点数字
	''', '(800) 555-1212')
print(m.groups())

print("10  扩展符号续 *********************")
m = re.findall(r'http://(?:\w+\.)*(\w+\.com)',\
'http://google.com http://www.google.com http://\
code.google.com')
print('@1')
print(m)

m = re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',\
'(800) 555-1212').groupdict()
print('@2')
print(m)

m = re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',\
'(\g<areacode>) \g<prefix>-xxxx', '(800) 555-1212')
print('@3')
print(m)

m = bool(re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)',\
'(800) 555-1212 800-555-1212 18005551212'))
print('@4')
print(m)

m = re.findall(r'\w+(?= van Rossum)',
               '''
               Guido van Rossum
               Tim Peters
               Alex Martelli
               Just van Rossum
               Raymond Hettinger
               ''')
print('@5')
print(m)

#这个m是为了符号^
m = re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
               '''
               sales@phptr.com
               postmaster@phptr.com
               eng@phptr.com
               noreply@phptr.com
               admin@phptr.com
               ''')
print('@6')
print(m)

m = re.finditer(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
               '''
               sales@phptr.com
               postmaster@phptr.com
               eng@phptr.com
               noreply@phptr.com
               admin@phptr.com
               ''')

[print('%s@aw.com'%e.group(1)) for e in m]

print("11  bool  *********************")
#上面一个之所以会匹配，是因为(x)是个独立的分组
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy')))
print(bool(re.search(r'(?:x|y)(?(1)y|x)', 'xx')))

print("12 杂***********************")
m = re.match(r'\bblow', 'blow') # backspace、 no match
if m: print(m.group())

