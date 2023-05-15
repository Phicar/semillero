a = int(input())
ss = 0
vis = []
mem = [-1 for i in range(1000001)]
def ot(x,y):
	if y>x or x<1 or y<1:
		return 0
	nu = numi(x,y)
	if mem[nu]!=-1:
		return mem[nu]
	mem[nu]=ot(x-1,y)+ot(x-1,y-1)-ot(x-2,y-1)+nu**2
	return mem[nu]
def sumi(xa,ya):
	global ss,vis
	q =[[xa,ya]]
	ss=0
	nu = numi(xa,ya)
	ss+=nu*nu
	vis[nu]=True
	while len(q)>0:
		x,y = q.pop()
		nu1 = numi(x-1,y)
		nu2 = numi(x-1,y-1)
		if x>1 and x!=y and not vis[nu1]:
			q.append([x-1,y])
			vis[nu1]=True
			ss+=nu1*nu1
		if x>1 and y>1 and not vis[nu2]:
			#sumi(x-1,y-1)
			q.append([x-1,y-1])
			vis[nu2]=True
			ss+=nu2*nu2
def numi(x,y):
	return (x*(x-1))//2+y
def coord(a):
	mini = 1
	maxi = 10**10
	f = -1
	ff = -1
	while mini<=maxi:
		m = (mini+maxi)//2
		tr = (m*(m+1))//2
		if a<=tr:
			f = m
			ff = tr
			maxi = m-1
		else:
			mini = m+1
	return f,a-(f*(f-1))//2
for _ in range(a):
	b = int(input())
	x = coord(b)
	ss = 0
	#vis = [False for i in range(b+1)]
	#print(x,numi(x[0],x[1]))
	#sumi(x[0],x[1])
	print(ot(x[0],x[1]))
