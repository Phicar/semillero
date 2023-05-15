import math
a = int(input())

for i in range(a):
	b = int(input())
	res = (b*(b+1))//2
	lo = (int)(math.log(b)/math.log(2))
	res-=2*(2**(lo+1)-1)
	print(res)
