def CountBits(n):
  n = (n & 0x5555555555555555) + ((n & 0xAAAAAAAAAAAAAAAA) >> 1)
  n = (n & 0x3333333333333333) + ((n & 0xCCCCCCCCCCCCCCCC) >> 2)
  n = (n & 0x0F0F0F0F0F0F0F0F) + ((n & 0xF0F0F0F0F0F0F0F0) >> 4)
  n = (n & 0x00FF00FF00FF00FF) + ((n & 0xFF00FF00FF00FF00) >> 8)
  n = (n & 0x0000FFFF0000FFFF) + ((n & 0xFFFF0000FFFF0000) >> 16)
  n = (n & 0x00000000FFFFFFFF) + ((n & 0xFFFFFFFF00000000) >> 32) # This last & isn't strictly necessary.
  return n
a = int(input())
mod = 10**9+7
for _ in range(a):
	ans = 0
	b = map(int,raw_input().split(" "))
	c =map(int,raw_input().split(" "))
	n = b[0]
	k = b[1]
	pren = [0 for i in range(64)]
	for x in c:
		pren[x]+=1
	for i in range(64):
		if CountBits(i)!=k:
			continue
		s = 1
		for j in range(64):
			if i&j!=i or pren[j]==0:
				continue
			quite =1
			if j!=i:
				quite+=1
			s = s*((1<<pren[j])-quite)%mod
		ans = (ans+s)%mod
	print(ans)
