a, b= map(int, input().split())
c, d= map(int, input().split())
e, f= map(int, input().split())
g, h= map(int, input().split())

one= b
two= b-c+d
thr= two-e+f
fou= thr-g

print(max(one,two,thr,fou))