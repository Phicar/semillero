a = int(input())
for i in range(a):
	b = int(input())
	use = [False for k in range(b)]
	dau = -1
	for j in range(b):
		paree =False
		c = map(int,raw_input().split(" "))
		for l in range(1,len(c)):
			if not use[c[l]-1]:
				use[c[l]-1]=True
				paree = True
				break
		if not paree:
			dau = j+1
	cab = -1
	for l in range(b):
		if not use[l]:
			cab = l+1
			break
	if dau==-1:
		print("OPTIMAL")
	else:
		print("IMPROVE")
		print(str(dau)+" "+str(cab))
