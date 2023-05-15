c = int(input())
for cc in range(c):
	a = raw_input()
	a0 = ord(a[0])-ord('a')
	a1 = ord(a[1])-ord('a')
	res = a0*25+a1
	if a0<a1:
		res-=1
	print(res+1)
