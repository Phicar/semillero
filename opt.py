import math
def dist(a,b):
	return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
a = map(int,raw_input().split(" "))
ang = 2.0*math.pi/a[0]
#print(ang)
mini = 0.0
maxi = 100.0
al = -1
tal = 0
print(a[1]*math.sqrt(2-2*math.cos(ang))/(2.0-math.sqrt(2-2*math.cos(ang))))
#while abs(maxi-mini)>0.0000001:
#	tal+=1
#	if tal>200:
#		break
#	mid = (mini+maxi)/2.0
#	#print(math.sin(ang),math.cos(ang))
#	dad = abs((a[1]+mid)*math.sin(ang))
#	dop = abs((a[1]+mid)*math.cos(ang))
#	otp = a[1]+mid
#	opd = 0.0
#	#print(mid,ang,dop,dad,otp,opd,dist([dop,dad],[otp,opd]),2*mid)
#	dd = dist([dop,dad],[otp,opd])
#	if dd<=2*mid:
#		maxi = mid-1
#		if abs(dd-2*mid)<0.00001:
#			al = mid
#	else:
#		mini = mid+1
#print(al)
