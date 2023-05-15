X = ["a","aa"]
def pref(s,x):
	si = True
	if len(x)>len(s):
		return False
	for i in range(len(x)):
		if x[i]!=s[i]:
			return False
	return True
def tal(s):
	if len(s)==0:
		return 1
	rs = 0
	for x in X:
		if pref(s,x):
			rs=rs+tal(s[len(x):])
	return rs

print(tal("aaaaaaaaa"))
