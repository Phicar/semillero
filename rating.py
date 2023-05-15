a = int(input())
ra = [int(input()) for i in range(a)]
me = 0
sol = []
for i in range(a):
	if abs(ra[i])%2==1:
		if me==0:
			print((ra[i]-1)/2)
		else:
			print((ra[i]+1)/2)

		me = me+1
		me = me%2
	else:
		print(ra[i]/2)
