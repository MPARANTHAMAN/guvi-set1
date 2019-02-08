A,B,C=raw_input().split()
A=int(A)
B=int(B)
C=int(C)
if(A>B) and (A>C):
	print(A)
elif(B>C) and (B>A):
	print(B)
else :
	print(C)
