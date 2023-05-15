a = map(int,raw_input().split(" "))
st = raw_input()
perm = {}
inv = {}
for x in range(26):
	perm[chr(ord("a")+x)]=chr(ord("a")+x)
	inv[chr(ord("a")+x)]=chr(ord("a")+x)
#print(perm)
for i in range(a[1]):
	b = raw_input().split(" ")
	xx = inv[b[0]]
	yy = inv[b[1]]
	px = perm[xx]
	py = perm[yy]
	#print(inter)
	perm[xx]=perm[yy]
	inv[perm[yy]]=xx
	perm[yy]=px #perm[xx]
	#inv[perm[yy]]=xx
	inv[px]=yy
	#inv[ix]=iy
	#print(b,perm,inv)
ans = ""
for i in range(len(st)):
	ans+=perm[st[i]]
#print(perm)
print(ans)
