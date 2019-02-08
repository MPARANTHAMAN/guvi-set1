pow=int(input())
exp=int(input())
def power(pow,exp):
    if(exp == 1):
    	return(pow)
    if(exp != 1):
    	return(pow*power(pow,exp-1))
print(power(pow,exp))
