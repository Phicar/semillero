a = map(int,raw_input().split())
if a[0]==1:
	print(a[1]-1)
	quit()
if a[1]==1:
	print(a[0]-1)
	quit()
print((a[1]-1)*a[0])
