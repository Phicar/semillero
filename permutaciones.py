N = 5
def perm(x,p,vis):
	if x==N:
		print(p)
		return
	for i in range(N):
		if vis&(1<<i)!=0:
			continue
		perm(x+1,p+" "+str(i+1),vis|(1<<i))
perm(0,"",0)
