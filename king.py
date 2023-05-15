a = int(input())
q = map(int,raw_input().split(" "))
k = map(int,raw_input().split(" "))
kk = map(int,raw_input().split(" "))
mapa = [[0 for i in range(a)] for j in range(a)]
dd = [-1,0,1]
for i in dd:
	for j in dd:
		for kr in range(0,a+1):
			nx = q[0]+kr*i
			ny = q[1]+j*kr
			if 1<=nx<=a and 1<=ny<=a:
				mapa[nx-1][ny-1]=-1
			else:
				break
def dfs(pp):
	global mapa,dd
	s = [pp]
	while len(s)>0:
		p = s.pop()
		mapa[p[0]-1][p[1]-1] = 1
		if p[0]==q[0] and p[1]==q[1]:
			break
		for i in dd:
			for j in dd:
				nx = p[0]+i
				ny = p[1]+j
				if 1<=nx<=a and 1<=ny<=a and mapa[nx-1][ny-1]==0:
					s.append([nx,ny]) #dfs([nx,ny])
#dfs(k)
if k[0]<q[0]<kk[0] or kk[0]<q[0]<k[0] or k[1]<q[1]<kk[1] or kk[1]<q[1]<k[1]:
	print("NO")
else:
	print("YES")
#if mapa[kk[0]-1][kk[1]-1]==1:
#	print("YES")
#else:
#	print("NO")
