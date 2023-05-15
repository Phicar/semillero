t = int(input())
for _ in range(t):
	a = int(input())
	b = map(int,raw_input().split(" "))
	xs = 0
	for i in range(a):
		xs^=b[i]
	if xs==0:
		print(0)
	elif a%2==1:
		print(xs)
	else:
		print(-1)
