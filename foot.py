a = int(input())
dic = {}
for i in range(a):
	s = raw_input()
	if s not in dic.keys():
		dic[s]=1
	else:
		dic[s]+=1
maxi = 0
maa = ""
for s in dic.keys():
	maxi = max(maxi,dic[s])
	if maxi==dic[s]:
		maa = s
print(maa)
