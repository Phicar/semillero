t = int(input())
for tt in range(t):
	nn = int(input())
	a = map(int,raw_input().split(" "))
	h = [False for i in range(nn)]
	c = [0 for i in range(nn)]
	for i in range(nn):
		if a[i]>0:
			l = i+1-a[i]
			if l<0:
				l = 0
			h[l]=True
			c[l]=max(c[l],i)
	#print(c)
	res = ["0" for i in range(nn)]
	j = 0
	while j<nn:
		if not h[j]:
			j+=1
			continue
		jl=j
		top = c[jl]
		jj = jl
		while jj<top+1: #for jj in range(jl,top+1):
			j+=1
			if c[jj]>0 and c[jj]>top:
				top = c[jj]
			res[jj]="1"
			jj+=1
	print(" ".join(res))
