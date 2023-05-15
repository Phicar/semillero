a = int(input())
for _ in range(a):
	b = int(input())
	c = map(int,raw_input().split(" "))
	x = 0
	ans = 0
	while x<b:
		#x = x
		s = 0
		while x<b and c[x]==0:
			s+=1
			x+=1
		x+=1
		ans = max(ans,s)
	print(ans)
	
