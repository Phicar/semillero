le = map(int,raw_input().split())
R = map(int,raw_input().split())
D = map(int,raw_input().split())
SS = [0 for i in range(le[0])]
SS[0]=R[0]
for i in range(1,le[0]):
	SS[i]=SS[i-1]+R[i]
#print(SS)
for j in range(len(D)):
	mini = 0
	maxi = le[0]
	posi = -1
	while mini<=maxi:
		c = (mini+maxi)/2
		if D[j]<=SS[c]:
			maxi = c-1
			posi = c
			#print(D[j],mini,maxi)
		else:
			mini = c+1
	rr = 0
	if posi>0:
		rr = SS[posi-1]
	print posi+1,D[j]-rr

