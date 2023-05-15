import math
memo = [-1 for i in range(100001)]
def tal(a):
	global memo
	if a<=3:
		return a
	mi = a+1
	if memo[a]!=-1:
		return memo[a]
	sa = str(a)
	for i in range(0,len(sa)):
		x = sa[:i]
		y = sa[i:]
		if len(x)==0 or len(y)==0 or y[0]=='0':
			continue
		mii = tal(int(x))+tal(int(y))
		mi = min(mi,mii)
	for i in range(2,(int)(math.sqrt(a))+1):
		if a%i==0:
			mii = tal(i)+tal(a/i)
			mi = min(mi,mii)
	for i in range(1,a//2+1):
		mii = tal(i)+tal(a-i)
		#print(a,i,a-i,mii)
		mi = min(mi,mii)
	#mi = min(mi,1+tal(a-1))
	memo[a]=mi
	return memo[a]
dp = [i+1 for i in range(100001)]
for i in range(4):
	dp[i]=i
for i in range(4,100001):
	z = 1
	while z<=i:
		dp[i]=min(dp[i],dp[i-z]+dp[z])
		z = int(str(z)+"1")
	for j in range(2,(int)(math.sqrt(i*1.0))+2):
		if i%j==0:
			dp[i]=min(dp[i],dp[j]+dp[i/j])
	sa = str(i)
	for j in range(len(sa)):
                x = sa[:j]
                y = sa[j:]
                if len(x)==0 or len(y)==0 or y[0]=='0':
                        continue
                dp[i] = min(dp[i],dp[int(x)]+dp[int(y)])
r = int(input())
print(dp[r])
#for r in range(1,200):
#	d = dp[r]
#	t = tal(r)
#	if d!=t:
#		print(r,d,t)
#print(dp[r])
