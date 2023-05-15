aa = int(input())
for cc in range(aa):
	a = map(int,raw_input().split(" "))
	p = map(int,raw_input().split(" "))
	ini = map(int,raw_input().split(" "))
	inv = set()
	for x in ini:
		inv.add(x-1)
	si = True
	#print(p)
	for x in range(1,a[0]):
		if not si:
			break
		piv = p[x]
		y = x-1
		while y>-1 and p[y]>piv:
			if y in inv:
				p[y+1]=p[y]
				y-=1
			else:
				#print(y,y+1,x,piv,inv)
				si = False
				break
		p[y+1]=piv
	if si:
		print("YES ")
	else:
		print("NO")
