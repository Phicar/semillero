def kt(n,k):
	if k<n:
		return k
	if k==n:
		return k+1
	c = k//n
	if k+c<(c+1)*n:
		return k+c
	return k+kt(n,c)+1
n,k = map(int,raw_input().split(" "))
print(kt(n,k))
