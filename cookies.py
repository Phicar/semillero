a = int(input())
def modpow(a,b,c):
	if b<=0:
		return (a**b)%c
	if b%2==0:
		sq = modpow(a,b/2,c)
		return (sq*sq)%c
	s = modpow(a,b-1,c)
	return (a*s)%c
if a<=1:
	print(1)
else:
	print(modpow(3,a-1,1000003))
