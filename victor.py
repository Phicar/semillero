a = int(input())
inf = 10**10
for _ in range(a):
	b = int(input())
	mini = [inf,inf,inf,inf]
	for _ in range(b):
		c = raw_input().split(" ")
		d = int(c[1][0])*2+int(c[1][1])
		mini[d] = min(mini[d],int(c[0]))
	ans = min(mini[3],mini[1]+mini[2])
	if ans>=inf:
		ans = -1
	print(ans)
