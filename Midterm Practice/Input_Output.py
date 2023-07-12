name = input("이름를 입력하세요: " )
number = int(input("숫자를 입력하세요: " ))

print(name,"님이 입력하신 숫자는",number,"입니다.") #표준출력
print("{} 님이 입력하신 숫자는 {} 입니다.".format(name,number)) #format매소드
print(f"{name} 님이 입력하신 숫자는 {number} 입니다.") #f-string
print("%s 님이 입력하신 숫자는 %d 입니다."%(name,number)) #스트링출력포맷