mod = 1000000007
aa = int(input())
for cc in range(aa):
	bb = map(int,raw_input().split(" "))
	x = bb[1]
	b2 = []
	ans=0
	while x>0:
		b2.append(x%2)
		x//=2
	for i in range(len(b2)):
		if b2[i]==1:
			ans+=bb[0]**i
	print(ans%mod)
