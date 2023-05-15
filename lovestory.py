a = int(input())
s = "codeforces"
for _ in range(a):
	b = raw_input()
	ans = 0
	for x in range(len(b)):
		if b[x]!=s[x]:
			ans+=1
	print(ans)
