a = map(int,raw_input().split(" "))
mat = []
vis = []
s = 0
dx = [0,1,0,-1]
dy = [-1,0,1,0]
def dfs(x,y):
	global s
	vis[x][y]=True
	s+=1
	for i in range(4):
		if mat[x][y]&(1<<i)!=0:
			continue
		xx = x+dx[i]
		yy = y+dy[i]
		if 0<=xx<=len(vis)-1 and 0<=yy<=len(vis[0])-1 and not vis[xx][yy]:
			dfs(xx,yy)
for i in range(a[0]):
	mat.append(map(int,raw_input().split(" ")))
	vis.append([False for i in range(a[1])])
ro = []
for i in range(a[0]):
	for j in range(a[1]):
		if vis[i][j]:
			continue
		s = 0
		dfs(i,j)
		ro.append(s)
ro.sort()
ro.reverse()
print(" ".join(map(str,ro))+" ")
