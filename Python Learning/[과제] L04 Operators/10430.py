a, b, c = map(int, input().split())

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

#왜 아님..?
#백준아 이상해..  -> 해결_괄호 하나 안 적었었음!!