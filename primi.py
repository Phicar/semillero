import math
a = int(input())
crib = [0 for i in range(10**7+1)]
sq = int(math.sqrt(10**7))+1
for x in range(2,sq):
	if crib[x]==0:
		for y in range(x,10000001,x):
			crib[y]=x
for cc in range(a):
	nn = int(input())
	b = map(int,raw_input().split(" "))
	f = {}
	for x in b:
		xx = x
		while crib[xx]!=0:
			q = 0
			c = crib[xx]
			while xx%c==0:
				q+=1
				xx//=c
			print(c,q)
	print("")
