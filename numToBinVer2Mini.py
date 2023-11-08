A=int(input('Decimal to binary\n'))
def B(decimal):
	A=decimal;B=''
	if A==0:return 0
	while A>0:C=A%2;A=A//2;B+=str(C)
	B=B[::-1];return B
print(B(A))