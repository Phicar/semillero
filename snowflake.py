a = int(input())
for _ in range(a):
	b = map(int,raw_input().split(" "))
	deg = [0 for i in range(b[0])]
	ady = [[] for i in range(b[0])]
	for _ in range(b[1]):
		c = map(int,raw_input().split(" "))
		deg[c[0]-1]+=1
		deg[c[1]-1]+=1
		ady[c[0]-1].append(c[1]-1)
		ady[c[1]-1].append(c[0]-1)
	uno = -1
	noh = -1
	xy = 0
	for i in range(b[0]):
		if deg[i]==1:
			uno = i
			noh = ady[i][0]
			xy+=1
	y = deg[noh]-1
	print(str(xy/y)+" "+str(y))
	#for j in range(len(ady[noh])):
	#	if deg[ady[uno][j]]!=1:
	#		noh = ady[uno][j]
	#		break
	
