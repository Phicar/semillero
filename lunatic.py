a = int(input())
def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)
for _ in range(a):
	b = int(input())
	c = map(int,raw_input().split(" "))
	mcm = 0
	entre = False
	for i in range(b):
		r = abs(c[i]-c[len(c)-1-i])
		if r==0:
			continue
		maxi = max(c[i],c[len(c)-1-i])
		entre = True
		mcm = gcd(mcm,r)
	if not entre:
		print(0)
	else:
		print(mcm)
