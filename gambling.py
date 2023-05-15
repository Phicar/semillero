import math
def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)
binom = [[0 for j in range(34)] for i in range(34)]
binom[0][0]=1
for i in range(1,34):
	binom[i][0]=1
	binom[i][i]=1
	for j in range(1,i):
		binom[i][j]=binom[i-1][j]+binom[i-1][j-1]
fac = [1 for i in range(34)]
for i in range(2,34):
	fac[i]=fac[i-1]*i
m,n,p = map(int,raw_input().split(" "))
dem = binom[m][p]*fac[p]
num = 0
for k in range(0,n):
	lef = 2*k+n-1-k
	if lef>=0 and lef<p:
		num+=2*n*binom[n-1][k]*binom[p-1][lef]*(2**(n-1-k))*fac[lef]*binom[m-2*n][p-1-(lef)]*fac[p-1-lef]
if num==0:
	print("0/1")
else:
	#print(num,dem)
	g = gcd(num,dem)
	print(str(num/(g))+"/"+str(dem/g))
