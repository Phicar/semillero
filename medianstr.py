a = int(input())
b = raw_input()
c = raw_input()
s = []
cc = 0
for i in range(a):
	j = ord(b[a-1-i])+ord(c[a-1-i])-2*ord('a')+cc
	cc=j//26
	j = j%26
	jj = j//2
	print(b[a-1-i],c[a-1-i],j,chr(ord('a')+j//2))
	s.append(chr(ord('a')+jj))
s.reverse()
print("".join(s))
