d = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
x = raw_input()
ans = 1
mod = 10**9+7
for i in range(len(x)):
	j = 0
	di = d.index(x[i])
	#print(x[i],di,bin(di))
	for l in range(6):
		if di%2==0:
			j+=1
			ans = (3*ans)%mod
		di//=2
print(ans)
