#rownanie postaci a*x+b=c
def rownanieX(a,b,c):
    return (c-b)/a

#uklad rownan z postaci
#ax+by=c
#dy+ex=f

def rownanieXY(a,b,c,d,e,f):
    y = (f-(d*c)/a)/(e-(d*b/a))
    x = (c-b*y)/a
    return (x, y)

print("Rownanie postaci: ")
print("5x+2y=7")
print("Ma rozwiazanie:")
print("x = ",rownanieX(5,2,7))
print()
print("Uklad rownan postaci:")
print("x+y=3")
print("x+2y=4")
para = rownanieXY(1,1,3,1,2,4)
print("Ma rozwiaznie")
print("x = ",para[0])
print("y = ",para[1])