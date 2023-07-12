members = ["권민기","김민수","박용희","최원건"]

for number, name in enumerate(members, start=1):
    print("TEAM A4의 {}번째 멤버는 {}입니다!".format(number, name))

#여기서 (members, start=1)의 순서대로가 아니라, 그냥 함수 enumerate()가 첫 번째 요소를 번호, 두 번째 요소를 번호에 해당하는 값 을 말한다.


