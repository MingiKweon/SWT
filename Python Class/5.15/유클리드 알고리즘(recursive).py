def u(a,b):
    a = max(a,b)
    b = min(a,b) 

    if b == 0:
        return a
    else:
        return u(b, a%b)
    
print(u(14,34))