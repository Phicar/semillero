mod = 998244353
dd = [[0 for i in range(1<<2)] for j in range(1<<2)]
dd[0][0]=0
dd[0][1]=1
dd[0][2]=1
dd[0][3]=1
dd[1][0]=0
dd[1][1]=0
dd[1][2]=2
dd[1][3]=0
dd[2][0]=0
dd[2][1]=2
dd[2][2]=0
dd[2][3]=0
dd[3][0]=1
dd[3][1]=1
dd[3][2]=1
dd[3][3]=0
dp = [[[0 for k in range(1<<2)] for j in range(2001)] for i in range(1001)]
for x in range(1<<2):
	a = x%2
	b = x//2
	if a==b:
		dp[1][1][x]+=1
	else:
		dp[1][2][x]+=1
for l in range(2,1001):
	for j in range(1,2*(l-1)+1):
		for k in range(1<<2):
			for kk in range(1<<2):
				dp[l][j+dd[kk][k]][k]=(dp[l][j+dd[kk][k]][k]+dp[l-1][j][kk])%mod
#for i in range(3):
#	for j in range(1,2*i+1):
#		print(i,j,dp[i][j])
a = map(int,raw_input().split(" "))
s = 0
for x in range(1<<2):
	s+=dp[a[0]][a[1]][x]
print(s%mod)
