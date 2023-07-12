f = open("vocabulary.txt","r", encoding="euc-kr")

lines = f.readlines()
for line in lines:
    print(line)

f.close()


with open("vocabulary.txt","r", encoding="euc-kr") as f:
    # lines = f.readlines()
    # for line in lines:
    #     print(line)
    all = f.read()
    print(all)
#with는 자동으로 f.close() 처리가 된다.


