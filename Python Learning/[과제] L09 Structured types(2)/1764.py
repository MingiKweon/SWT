x , y = map(int, input().split())

hear = set()
for i in range(x):
    hear.add(input())

see = set()
for j in range(y):
    see.add(input())

hs = hear & see
hs = sorted(hs)
print(len(hs))
for n in list(hs):
    print(n)


# arr = []
# for m in list(hear | see):
#     if m in list(hear) and m in list(see):
#         arr.append(m)

# print(len(arr))
# for _ in arr:
#     print(_)   