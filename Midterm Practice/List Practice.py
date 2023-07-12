#리스트는 아이템을 모은 순차 데이터타입

print(dir(print()))

graduate = ["길동","영수","민아"]
undergraduate = ["민수","영아","정국"]

print(graduate + undergraduate)
print(graduate*2)
print(len(graduate*2))

a = ["a","b","c","d","e"]
a.append("f")
print(a)
a.append("d")
print(a)
a.insert(-1,1)
print(a)
a.extend(["1","2","4","1"])
print(a)
a.append(["a","b","c"])
print(a)

#추가 -- .append(), .insert(a,b), .extend() 

a.remove("1")
print(a)
#a.remove(1) #만약 없으면 오류남

del a[2]
print(a)
y = a.pop(1) #이것도 인덱스 영향이네
print(y)
print(a)
x = a.pop() #괄호 안에 뭐 안 적어놓았으면 맨 끝값이 제거되고 리턴
print(x)
print(a)
a.clear()
print(a)

#제거 -- .remove(), del <list>[] ,.pop(), .clear()

#find 함수는 찾는 문자가 문자열 안에 포함되지 않은 경우 -1을 출력한다
#index 함수는 찾는 문자가 문자열 안에 포함되지 않은 경우에는 AttributeError를 낸다.

#find 함수는 문자열만 된다
#index 함수는 문자열뿐만 아니라 반복 가능한 iterable한 리스트, 튜플, 문자열 등등을 사용할 수 있다.