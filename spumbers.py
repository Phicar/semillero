a = raw_input().split(" ")
aa = a[0]
bb = a[2]
cc = a[4]
#print(aa,bb,cc)
termine = False
for i in range(len(aa)):
	for j in range(len(bb)):
		if termine:
			break
		ab = int(bb[:j]+aa[i:])
		ba = int(aa[:i]+bb[j:])
		#print(ab,ba)
		if a[1]=='+':
			if ab+ba==int(cc):
				print(str(ab)+" + "+str(ba)+" = "+cc)
				termine = True
		else:
			if ab*ba==int(cc):
                                print(str(ab)+" * "+str(ba)+" = "+cc)
                                termine = True
for i in range(len(aa)):
        for j in range(len(cc)):
                if termine:
                        break
                ab = int(cc[:j]+aa[i:])
                ba = int(aa[:i]+cc[j:])
                if a[1]=='+':
                        if ab+int(bb)==ba:
                                print(str(ab)+" + "+bb+" = "+str(ba))
                                termine = True
		else:
			if ab*int(bb)==ba:
                                print(str(ab)+" * "+bb+" = "+str(ba))
                                termine = True

for i in range(len(bb)):
        for j in range(len(cc)):
                if termine:
                        break
                ab = int(cc[:j]+bb[i:])
                ba = int(bb[:i]+cc[j:])
                if a[1]=='+':
                        if ab+int(aa)==ba:
                                print(aa+" + "+str(ab)+" = "+str(ba))
                                termine = True
		else:
			if ab*int(aa)==ba:
                                print(aa+" * "+str(ab)+" = "+str(ba))
                                termine = True
				
