TeamA4 = {1116:'김민수', 419:'박용희'}
print(TeamA4[419])
TeamA4.update({1003:'최현민', 1003:'최원건'})
print(TeamA4)

if 419 in TeamA4:
    print(TeamA4[419])
else:
    print("Invaild Key")


set1 = {1,2,4}
set2 = {1,4,5,8,9}

print(set1^set2) #대칭차집합:겹치는 것을 뺀 나머지 값들(https://hanmaths.tistory.com/15)