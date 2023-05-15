a = map(int,raw_input().split())
r =0
if a[0]!=a[2]:
	r+=1
if a[1]!=a[3]:
	r+=1
b = 0
if (a[0]+a[1])%2 ==(a[2]+a[3])%2:
	b = 1
	if abs(a[0]-a[2])!=abs(a[1]-a[3]):
		b= 2
	#if abs(8-a[0])
k = min(abs(a[0]-a[2]),abs(a[1]-a[3]))+abs(abs(a[0]-a[2])-abs(a[1]-a[3]))
print(str(r)+" "+str(b)+" "+str(k))
