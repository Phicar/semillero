a = raw_input()
k = (1<<(len(a)))-1
if len(a)==1:
	k = 1
for i in range(len(a)):
	if a[i]=='7':
		k+=(1<<(len(a)-i-1))
print(k)
