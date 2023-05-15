a = int(input())
for _ in range(a):
	b = int(input())
	c = map(int,raw_input().split(" "))
	ans = 0
	fr = [0]
	igu = True
	for i in range(1,b):
		fr.append(fr[-1]+abs(c[i]-c[i-1]))
		igu = igu and (c[i]==c[i-1])
	y = 0
	s= 0
	si = True
	while si:
		si = False
		#print("->",y)
		mini = y+1
		maxi = b-1
		x = -1
		while mini<=maxi:
			xx = (mini+maxi)//2
			if abs(c[xx]-c[y])==fr[xx]-fr[y]:
				mini = xx+1
				x = xx
			else:
				maxi = xx-1
		if x!=-1:
			#print(y,x)
			si = True
			s+=x-y-1
			y = x
		#for x in range(b-1,y,-1):
		#	#print(x,y,fr[x]-fr[y],abs(c[x]-c[y]))
		#	if abs(c[x]-c[y])==fr[x]-fr[y]:
		#		s += x-y-1
		#		y = x
		#		si = True
		#		#print(x,y,s)
		#		break
	if igu:
		print(1)
	else:
		print(b-s)
