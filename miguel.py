def kdivisor(n, k):
	def cantdiv(x):
		return x//n
	mini,maxi=1,10**10
	while mini<maxi:
		med = (mini + maxi) // 2
		if med - cantdiv(med) < k:
			mini = med + 1
		else:
			maxi = med
	return mini
print(kdivisor(10**10,10**10))
