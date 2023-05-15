c = int(input())
for cc in range(c):
	a = int(input())
	b = map(int,raw_input().split())
	d = int(input())
	e = map(int,raw_input().split())
	p = 0
	for x in e:
		p=(p+x)%a
	print(b[p])
