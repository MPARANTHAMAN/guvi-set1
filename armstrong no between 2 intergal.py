a1,b1=raw_input().split()
a1=int(a1)
b1=int(b1)
for num in range(a1,b1):
	sum=0
	temp=num
	while temp>0:
		digit = temp %10
		sum =sum+digit**3
		temp/=10
	if num == sum:
	  print(num)
