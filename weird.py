a = map(int,raw_input().split(" "))
while  a[0]>=2*a[1] or a[1]>=2*a[0]:
	if a[0]==0 or a[1]==0:
		break
	if a[0]>=2*a[1]:
		q = (a[0]//a[1])
		if q%2==1:
			q-=1
		a[0]-=q*a[1]
	else:
		q = (a[1]//a[0])
		if q%2==1:
			q-=1
		a[1]-=q*a[0]
	#print(q,a)
print(" ".join(map(str,a)))
