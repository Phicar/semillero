a  = map(int,raw_input().split())
pad = [[i,1] for i in range(a[0])]
def find(x):
	if x==pad[x][0]:
		return x
	return find(pad[x][0])
def union(x,y):
	global pad
	px = find(x)
	py = find(y)
	if px==py:
		return
	pad[py][0]=px
	pad[px][1]+=pad[py][1]
for i in range(a[1]):
	b = map(int,raw_input().split())
	union(b[0]-1,b[1]-1)
res = 1
for i in range(a[0]):
	if i==pad[i][0]:
		#print(i,pad[i][1])
		res*=(1<<(pad[i][1]-1))
print(res)
