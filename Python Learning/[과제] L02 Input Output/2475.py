a, b, c, d, e= map(int, input().split())

sum= a**2+b**2+c**2+d**2+e**2 #a*a==a**2
print(sum%10)


#def를 사용할 수 있음!
#lamda

def f1(x1,x2,x3,x4,x5):
    return (x1*x1+x2*x2+x3*x3+x4*x4+x5*x5) % 10
a, b, c, d, e= map(int, input().split())

print(f1(a,b,c,d,e))