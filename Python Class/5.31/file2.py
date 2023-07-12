with open("vocabulary.txt","r", encoding="euc-kr") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

    f.seek(0)
    print(f.readline())


    #readline vs readlines