A=input
B=int
C=B(A('Decimal to selected base.\n'))
D=B(A('What base would you like?\n'))
def E(base):
	A=base
	if A<10 and A>0:return chr(A+ord('0'))
	else:return chr(A-10+ord('A'))
def F(base,input,output):
	A=output
	while input>0:A+=E(input%base);input=B(input/base)
	A=A[::-1];return A
print(F(D,C,''))