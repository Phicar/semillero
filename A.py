c = int(input())
for cc in range(c):
	t = int(input())
	tt = t//2
	L = []
	if t==1:
		print("1")
		quit()
	if t%2==0:
		s = ""
		L = []
		for i in range(t-(tt-1),0,-1*tt):
			L.append(i)
		for i in range(t-(tt-1)+1,t+1,1):
			for j in range(i,0,-1*tt):
				L.append(j)
		for i in L:
			s = s+str(i)+" "
		print(s[0:-1])
	else:
		for i in range(t,0,-1*tt):
			L.append(i)
		for i in range(t-(tt-1),t):
			for j in range(i,1,-1*tt):
				L.append(j)
		s = ""
		for i in L:
			s = s+str(i)+" "
		print(s[0:-1])
