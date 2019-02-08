a1,b1=raw_input().split()
a1=int(a1)
b1=int(b1)
for num in range(a1,b1+1):
	if num >1:
		for i in range(2,num):
			if(num %i)==0:
				break
		else:
		  print num,
