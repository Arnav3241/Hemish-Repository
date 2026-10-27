l=int(input("Give L : "))
b=int(input("Give B : "))
h=int(input("Give H : "))
def Cuboid(l,b,h):
    s=2*(l*b+b*h+l*h)
    v=l*b*h
    print(s,v)
Cuboid(l,b,h)
