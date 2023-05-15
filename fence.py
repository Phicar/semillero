a = map(int,raw_input().split(" "))
b = map(int,raw_input().split(" "))
c = [b[0]]
for i in range(1,a[0]):
	c.append(c[-1]+b[i])
mini = c[a[1]-1]
minii = 1
#print(c)
#print(mini,minii)
for i in range(a[1],a[0]):
	if mini>c[i]-c[i-a[1]]:
		mini = c[i]-c[i-a[1]]
		minii = i+1-a[1]+1
		#print(mini,minii)
print(minii)
