import math
a = int(input())
sa = (int)(math.sqrt(a))+1
d=0
for k in range(1,sa):
	if a%k==0:
		d+=2
	if k*k==a:
		d-=1
print(d)
