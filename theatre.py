t = int(input())
for _ in range(t):
	a = map(int,raw_input().split(" "))
	ma = []
	res = 0
	x = a[2]
	y = a[3]
	for i in range(a[0]):
		p = raw_input()
		j = 0
		while j<len(p):
			if p[j]=='*':
				j+=1
				continue
			jj = j
			while jj<len(p) and p[jj]=='.':
				jj+=1
			li = jj-j
			if 2*x<y:
				res+=li*x
			else:
				res+=y*(li//2)+x*(li%2)
			j = jj
	print(res)

	
