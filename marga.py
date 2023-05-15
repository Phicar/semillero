def pares(a):
	if a<=1:
		return 0
	if a%2==1:
		return pares(a-1)
	return (a//2)*(a//2+1)
def impares(a):
	if a<=1:
		return a
	if a%2==0:
		return impares(a-1)
	re = pares(a-1)
	return re+(a//2+1)
a = int(input())
for i in range(a):
	b = map(int,raw_input().split(" "))
	ss = pares(b[1])
	ss-=pares(b[0]-1)
	ss+=impares(b[0]-1)
	ss-=impares(b[1])
	print(ss)
