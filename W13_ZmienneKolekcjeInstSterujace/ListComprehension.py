A=[x**3 for x in range(0,11)]
print("Zbior A:")
print(A)
B=[3**i for i in range(0,6)]
print("Zbior B:")
print(B)
C=[x for x in A if x%3==0]
print("Zbior C:")
print(C)