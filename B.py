t = int(input())
s = (str(raw_input())).split()
tt= map(int,s)
i = 0
L = []
while i<t:
	j = i
	while j<t and tt[j]==tt[i]:
		j+=1
	L.append(j-i)
	i = j
ma = 0
for i in range(len(L)-1):
	ma = max(ma,min(L[i],L[i+1]))
print(ma*2)
