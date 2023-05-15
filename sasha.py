aa = map(int,raw_input().split(" "))
a =aa[0]
b = aa[1]
if a<=b:
	print(a)
else:
	print(b+((a-b+1)*(a-b))/2-1)
