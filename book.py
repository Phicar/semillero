q = int(input())
for i in range(q):
	a,b = map(int,raw_input().split(" "))
	u = b%10
	qq = a//b
	r = a%b
	di = [(u*(1+i))%10 for i in range(9)]
	su = sum(di)
	res = su*(qq//10)+sum(di[0:qq%10])
	print(res)
