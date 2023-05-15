a = int(input())
for i in range(a):
	b = int(input())
	c = map(int,raw_input().split(" "))
	s = sum(c)
	if s%2==0:
		print(0)
	else:
		mini = 10000000000
		for j in range(len(c)):
			mm = 0
			jj = c[j]
			while (jj-c[j])%2==0:
				mm+=1
				jj/=2
			mini = min(mini,mm)
		print(mini)
