aa= map(int,raw_input().split(" "))
mini = 0
maxi = 10**10
la = -1
while mini<=maxi:
	m = (mini+maxi)//2
	paila = False
	for t in range(m,m+aa[2]+1):
		if aa[1]*t<aa[0]*(t-m):
			paila = True
	if paila:
		mini = m+1
	else:
		la = m
		maxi = m-1
print(la)
