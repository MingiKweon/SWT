a = [8,4,9,5]

s = max(a)
for i in a:
    if s > i:
        s = i
print(s)

print(sum(a)) #sum([[],[]]일때는 안됨) // 0 + []으로 실행되는 구조라
