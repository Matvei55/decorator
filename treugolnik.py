from math import*
def decorator (sct):
    def treu (a,b,c):
        print(acos(c/a))
        print(asin(b/a))
        print(atan((b/a)/(c/a)))
        sct(a,b,c)
    return treu

@decorator

def sct (a,b,c):
    sinus=b/a
    cosinus=c/a
    tgs=sinus/cosinus
    print(sinus,cosinus,tgs)


a=float(input())
b=float(input())
c=float(input())

sct(a,b,c)