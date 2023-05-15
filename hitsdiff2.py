a = int(input())
ss = 0
vis = []
mem = [-1 for i in range(1000001)]
def numi(x,y):
        return (x*(x-1))//2+y
dp = [[0 for i in range(1500)] for j in range(1500)]
dp[1][1]=1
dp[2][1]=5
dp[2][2]=10
for i in range(3,1500):
	nu1 = numi(i,1)
	dp[i][1]=dp[i-1][1]+nu1*nu1
	for j in range(2,i):
		nu = numi(i,j)
		dp[i][j]=dp[i-1][j]+dp[i-1][j-1]+nu**2
		if i-2>=j-1:
			dp[i][j]-=dp[i-2][j-1]
	dp[i][i]=dp[i-1][i-1]+numi(i,i)**2
def ot(x,y):
	if y>x or x<1 or y<1:
		return 0
	nu = numi(x,y)
	if mem[nu]!=-1:
		return mem[nu]
	mem[nu]=ot(x-1,y)+ot(x-1,y-1)-ot(x-2,y-1)+nu**2
	return mem[nu]
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
	print(dp[x[0]][x[1]])
