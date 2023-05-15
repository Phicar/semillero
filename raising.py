a = int(input())
res = 0
while a>0:
	res+=a%2
	a//=2
print(res)
