def dfs(x,y):
	global vis,ady
	if x==y:
		return True
	#vis[x]=True
	vi = False
	for z in ady[x]:
		if not vis[z]:
			vi = vi or dfs(z,y)
	return vi
n = 5
ady = [[1,2],[0,2],[0,1],[4],[3]]
for x in range(5):
	for y in range(5):
		vis = [False for i in range(5)]
		print(x,y,dfs(x,y))
