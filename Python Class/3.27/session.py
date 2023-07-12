import datetime

now = datetime.datetime.now()

if now.month == 3 or now.month == 4 or now.month == 5:
    print("봄")
elif now.month == 6 or now.month == 7 or now.month == 8:
    print("여름")
elif now.month == 9 or now.month == 10 or now.month == 11:
    print("가을")
else:
    print("겨울")