def main():
	number=int(input())
	sum1=0
	temp=number
	while temp>0:
		digit = temp%10
		sum1 +=digit**3
		temp //=10
	if number ==sum1:
		print("yes")
	else:
		print("no")
if __name__ == '__main__':
		main()
    
