a =map(int,raw_input().split(" "))
vis = set()
si = False
def dfs(x,y,c):
	global si
	if x>y:
		return
	if si:
		return
	if x==y:
		si = True
		print("YES")
		print(len(c))
		print(" ".join(c))
		return
	#vis.add(x)
	cc = c[:]
	cc.append(str(2*x))
	dfs(2*x,y,cc)
	cc.pop()
	cc.append(str(10*x+1))
	dfs(10*x+1,y,cc)
dfs(a[0],a[1],[str(a[0])])
if not si:
	print("NO")
