def find(x):
	r = x
	while r!=pad[r][0]:
		#x = pad[x][0]
		r = pad[r][0]
	while pad[x][0]!=x:
		pa = pad[x][0]
		pad[x][0]=r
		x = pa
	return r
def union(x,y):
	if x==y:
		return
	px = find(x)
	py = find(y)
	if pad[px][2]>pad[py][2]:
		pad[py][0]=px
		pad[px][1]+=pad[py][1]
	else:
		if pad[px][2]==pad[py][2]:
			pad[px][2]+=1
		pad[px][0]=py
                pad[py][1]+=pad[px][1]
a,b = map(int,raw_input().split(" "))
pad = [[i,1,0] for i in range(a)]
for i in range(b):
	c = map(int,raw_input().split(" "))
	for j in range(1,len(c)):
		union(c[1]-1,c[j]-1)
ans = []
#print(pad)
for i in range(a):
	ans.append(str(pad[find(i)][1]))
print(" ".join(ans))
