from math import*
def decorator (discriminant):
    def wieta (a,b,c):
        print('x1 + x2=-p')
        print('x1 * x2=q')
        discriminant(a,b,c)
    return wieta





@decorator

def discriminant (a,b,c):
    d=b**2 - -4*a*c

    x1=(-b + sqrt(d))/2*a

    x2=(-b - sqrt(d))/2*a

    print(x1,x2)


a=int(input())
b=int(input())
c=int(input())

discriminant(a,b,c)