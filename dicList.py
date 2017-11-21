d={'matthew':'blue','rachel':'green','raymond':'red'}

for k in d:
	print(k)

for k in d.keys():
	if k.startswith('r'):
		del d[k]
print('')

print("Let's remove the keys start with 'r'.")

for k,v in d.items():
	print(k),('--->'),(v)
