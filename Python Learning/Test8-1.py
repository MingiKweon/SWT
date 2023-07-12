year = 0
balance = 1000000

while balance < 2000000:
    year += 1
    balance = int(balance * 1.05)

print("{}년 저금하시면 {}원이 됩니다.".format(year,balance))