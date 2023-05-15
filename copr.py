a = int(input())
def gcd(a,b):
	while b!=0:
		bb = b
		b = a%b
		a = bb
	return a
	#if b==0:
	#	return a
	#return gcd(b,a%b)
adj = [[False for x in range(1001)] for y in range(1001)]
for x in range(1,1001):
	for y in range(x,1001):
		adj[x][y]=adj[y][x]=(gcd(x,y)==1)
for i in range(a):
	b = int(input())
	c = map(int,raw_input().split(" "))
	maxi = -1
	ult = [-1 for i in range(1001)]
	for i in range(b-1,-1,-1):
		if ult[c[i]]==-1:
			ult[c[i]]=i
	for i in range(1,1001):
		if ult[i]==-1:
			continue
		for j in range(i,1001):
			if adj[i][j] and ult[i]>-1 and ult[j]>-1:
				maxi = max(maxi,ult[i]+ult[j]+2)
	print(maxi)
