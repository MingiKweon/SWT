n = input()
x = list(range(97,123))

for i in x:
    print(n.find(chr(i)) , end=" ")
print()


for j in x:
    try:
        m = n.index(chr(j))
        print(m, end=" ")
    except:
        print(-1, end=" ")


#find 함수는 찾는 문자가 문자열 안에 포함되지 않은 경우 -1을 출력한다
#index 함수는 찾는 문자가 문자열 안에 포함되지 않은 경우에는 AttributeError를 낸다.

#find 함수는 문자열만 된다
#index 함수는 문자열뿐만 아니라 반복 가능한 iterable한 리스트, 튜플, 문자열 등등을 사용할 수 있다.

#입력 후 오류가 나왔을 때, 출력값을 달리 할 수 있다. <try,except,else 등등> <https://wikidocs.net/30>