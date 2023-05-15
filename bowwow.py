s = raw_input()
unos = 0
res = 0
for i in range(len(s)):
	if s[i]=='1':
		unos+=1
	if i%2==0:
		res+=1
if unos==1 and len(s)%2==1:
	res-=1
if unos==0:
	res = 0
print(res)
