a = int(input())
b = raw_input()
c = raw_input()
res = []
cc = 0
for i in range(a-1,-1,-1):
	j = ord(b[i])+ord(c[i])-2*ord('a')
	j+=cc
	print(j)
	cc = j//26
	j = j%26
	j//=2
	print(cc,j)
	res.append(chr(ord('a')+j))
res.reverse()
print("".join(res))
