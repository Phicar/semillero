def CountBits(n):
  n = (n & 0x5555555555555555) + ((n & 0xAAAAAAAAAAAAAAAA) >> 1)
  n = (n & 0x3333333333333333) + ((n & 0xCCCCCCCCCCCCCCCC) >> 2)
  n = (n & 0x0F0F0F0F0F0F0F0F) + ((n & 0xF0F0F0F0F0F0F0F0) >> 4)
  n = (n & 0x00FF00FF00FF00FF) + ((n & 0xFF00FF00FF00FF00) >> 8)
  n = (n & 0x0000FFFF0000FFFF) + ((n & 0xFFFF0000FFFF0000) >> 16)
  n = (n & 0x00000000FFFFFFFF) + ((n & 0xFFFFFFFF00000000) >> 32) # This last & isn't strictly necessary.
  return n
a = map(int,raw_input().split(" "))
dic = {}
li = []
for x in range(a[0]):
	li.append(raw_input())
	dic[li[-1]]=x
re = []
for x in range(a[1]):
	b = raw_input().split(" ")
	x1 = dic[b[0]]
	x2 = dic[b[1]]
	re.append((1<<x1)|(1<<x2))
ans = 0
ansi = 0
for x in range(1<<a[0]):
	si = True
	for y in re:
		if x&y==y:
			si = False
			break
	if si:
		bc = CountBits(x) #x.bit_count()
		if bc>ans:
			ans =bc
			ansi = x
print(ans)
aa = []
for x in range(a[0]):
	if ansi&(1<<x) !=0:
		aa.append(li[x])
aa.sort()
for x in range(ans):
	print(aa[x])
