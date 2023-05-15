a = int(input())
#b = map(int,raw_input().split(" "))
#mat =[]
#vis = []
#s = 0
dx = [0,-1,0,1]
dy = [1,0,-1,0]
def dfs(xa,ya):
	global vis,mat,s
	q = []
	q.append((xa,ya))
	vis[xa][ya]=True
	s=mat[xa][ya]
	while len(q)>0:
		x,y = q.pop()
		#vis[x][y]=True
		#s+=mat[x][y]
		for i in range(4):
			xx = x+dx[i]
			yy = y+dy[i]
			if 0<=xx<len(mat) and 0<=yy<len(mat[0]) and not vis[xx][yy] and mat[xx][yy]!=0:
				q.append([xx,yy]) #dfs(xx,yy)
				vis[xx][yy]=True
				s+=mat[xx][yy]
for _ in range(a):
	mat = []
	vis = []
	s = 0
	b = map(int,raw_input().split(" "))
	for _ in range(b[0]):
		mat.append(map(int,raw_input().split(" ")))
		vis.append([False for i in range(b[1])])
	vol = 0
	for i in range(b[0]):
		for j in range(b[1]):
			if not vis[i][j] and mat[i][j]!=0:
				s = 0
				dfs(i,j)
				vol = max(vol,s)
	print(vol)
