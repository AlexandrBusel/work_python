palindroms = range(1, 2018)
for n in palindroms:
	a=str(n)
	if a[0:] == a[::-1]:
		print (a[::-1])
	
