def CountBits(n):
  n = (n & 0x5555555555555555) + ((n & 0xAAAAAAAAAAAAAAAA) >> 1)
  n = (n & 0x3333333333333333) + ((n & 0xCCCCCCCCCCCCCCCC) >> 2)
  n = (n & 0x0F0F0F0F0F0F0F0F) + ((n & 0xF0F0F0F0F0F0F0F0) >> 4)
  n = (n & 0x00FF00FF00FF00FF) + ((n & 0xFF00FF00FF00FF00) >> 8)
  n = (n & 0x0000FFFF0000FFFF) + ((n & 0xFFFF0000FFFF0000) >> 16)
  n = (n & 0x00000000FFFFFFFF) + ((n & 0xFFFFFFFF00000000) >> 32) # This>
  return n
n,m,k = map(int,raw_input().split(" "))
a = map(int,raw_input().split(" "))
rt = [[] for i in range(n+1)]
for x in range(1<<n):
	rt[CountBits(x)].append(x)
mat = [[0 for i in range(n)] for j in range(n)]
for _ in range(k):
	c = map(int,raw_input().split(" "))
	mat[c[0]-1][c[1]-1] = c[2]
dp = [[0 for i in range(n)] for j in range(1<<n)]
for i in range(n):
	dp[1<<i][i]=a[i]
for i in range(2,m+1):
	for x in rt[i]:
		for j in range(n):
			if (1<<j)&x==0:
				continue
			xx = x^(1<<j)
			for l in range(n):
				if l==j or (1<<l)&x==0:
					continue
				dp[x][j]=max(dp[x][j],dp[xx][l]+a[j]+mat[l][j])
s = 0
for x in rt[m]:
	for i in range(n):
		s = max(s,dp[x][i])
print(s)
