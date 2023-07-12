n = int(input())

arr = {}
for i in range(n):
    x , y = input().split()
    arr.update({x:y})

work = []
for j in arr:
    if arr[j] == "enter":
        work.append(j)

work.sort(reverse=True)
for m in work:
    print(m)

#문제상의 사전의 역순이라는 뜻은 아마 실제 a,b,c,d, .. 의 알파벳 순서의 역순을 의미하는 것 같다.