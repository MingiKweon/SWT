a = [1,2,3,4,5,6]


a.insert(-1,1000)
print(a)

#append > insert (속도) (메모리 저장 방식 상 insert(0,i)일 때마다 있던 배열을 뒤로 미뤄야한다)

#remove도 마찬가지 원리이다. (list는 비어있음을 허용하지 않음)
#위 문제를 제외하더라도 찾는데 오래걸림

