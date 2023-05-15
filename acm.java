import math
a = list(map(int, input().split(" ")))
mod = 1000000007
s = 0
bin = [[1]]
for i in range(1,4001):
	bb = [1]
	for j in range(1,i):
		bb.append((bin[-1][j]+bin[-1][j-1])%mod)
	bb.append(1)
	bin.append(bb)
#print(bin[6])
cr = [0 for i in range(4001)]
sq = int(math.sqrt(2000.0))+1
for x in range(2,sq):
	if cr[x]==0:
		for y in range(x,2001,x):
			cr[y]=x
for i in range(1,a[0]+1):
	ii = i
	#print(ii)
	f = {}
	while cr[ii]!=0:
		#print(ii,cr[ii])
		if cr[ii] not in f.keys():
			f[cr[ii]]=1
		else:
			f[cr[ii]]=f[cr[ii]]+1
		ii//= cr[ii]
	ts = 1
	for x in f.keys():
		ts = (ts*bin[a[1]-1+f[x]][f[x]])%mod
	s=(s+ts)%mod
	#print(i,ts)
print(s%mod)
