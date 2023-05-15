t = int(input())
for tt in range(t):
	a = int(input())
	b = raw_input()
	mi = 0
	print(b)
	ul = [[-1,-1] for i in range(a)]
	ul[0][int(b[0])]=0
	for i in range(1,a):
		ul[i][int(b[i])]=i
		ul[i][1-int(b[i])]=ul[i-1][1-int(b[i])]
	print(ul)
