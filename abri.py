a = map(int,raw_input().split(" "))
b = map(int,raw_input().split(" "))
pad = [-1 for i in range(a[0])]
vis = [False for i in range(a[0])]
for i in range(a[1]):
	c = map(int,raw_input().split(" "))
	pad[c[1]-1]=c[0]-1
	vis[c[0]-1]=True
novis = []
for i in range(a[0]):
	if not vis[i]:
		novis.append(i)
mini = sum(b)
for i in range(len(novis)):
	for j in range(i+1,len(novis)):
		tmp = 0
		visi = [False for k in range(a[0])]
		ii = novis[i]
		jj = novis[j]
		while ii!=-1 and not visi[ii]:
			tmp+=b[ii]
			visi[ii]=True
			ii = pad[ii]
		while jj!=-1 and not visi[jj]:
                        tmp+=b[jj]
                        visi[jj]=True
                        jj = pad[jj]
		mini = min(mini,tmp)
		#print(novis[i],novis[j],tmp)
print(mini)
