a = int(input())
aa = map(int,raw_input().split(" "))
ans = []
def val(a):
	s = 0
	while a%2==0:
		s+=1
		a/=2
	return s
for i in range(a):
	x = aa[i]
	if x==0:
		ans.append(str("0"))
		continue
	mini = 15
	for i in range(0,16):
		mini = min(mini,i+15-val(x+i))
	ans.append(str(mini))
print(" ".join(ans))
