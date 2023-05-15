a = int(input())
for _ in range(a):
	b = map(int,raw_input().split(" "))
	c = map(int,raw_input().split(" "))
	c.sort()
	mi = 0
	ma = b[0]-1
	fr = [c[0]]
	for i in range(1,b[0]):
		fr.append(fr[-1]+c[i])
	maxi = 0
	for i in range(0,b[1]+1):
		l = 2*(b[1]-i)
		ll = l-1
		if l<=b[0]-1-i:
			rm = fr[b[0]-1-i]
			if ll>-1:
				rm-=fr[ll]
			maxi = max(maxi,rm)
	print(maxi)
