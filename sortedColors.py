#from pythonic import colors
colors=['red','green','blue','yellow']
#print(sorted(colors))
#print(sorted(colors,reverse=True))

for scolor in sorted(colors):
	print(scolor)
print('')
for rcolor in sorted(colors,reverse=True):
	print(rcolor)
print('')
for dcolor in sorted(colors,key=len):
	print(dcolor) 
print('')
