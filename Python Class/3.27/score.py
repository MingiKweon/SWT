score = int(input())

if score > 100 :
    print("Not Valid Number") ##이거 else때문에 밑에 학점도 출력되는데 고쳐야함.
elif 90 <= score and score <= 100 : ##90<=score<=100 파이썬에서는 이렇게 적어도 가능
    print("학점: A")
elif 80 <= score <= 89 :
        print("학점: B")
else:   print("학점: C")