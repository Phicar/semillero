a = int(input())
for _ in range(a):
	b = int(input())
	c = map(int,raw_input().split(" "))
	c.sort()
	ans = -1
	x = 0
	while x<b:
		t = c[x]
		while x+1<b and c[x+1]==c[x]:
			x+=1
		mt = b+1
		if x+1<b:
			mt = c[x+1]
		for tt in range(c[x],mt):
			#print(tt,x,b-1-x)
			if b-1-x==tt:
				ans = tt
				break
		if ans!=-1:
			break
		x+=1
	print(ans)
