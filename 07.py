from math import*
def decorator (sct):
    def treu (u1,u2,t):
        S=u1*t
        sct(u1,u2,t)
        print('Расстояние равно',S)
    return treu

@decorator

def sct (u1,u2,t):
    a = (u1-u2)/t
    print('Ускорение равно',a)
try:
    u1=int(input())
    u2=int(input())
    t=int(input())
    if t==0:
        raise Exception('время не должно быть равно нулю')

except ValueError:
    print('Это должны быть числа')



except Exception as e:
    print(e)
else:
    sct(u1,u2,t)