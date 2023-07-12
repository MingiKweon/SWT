def printMyAddress(firstname, lastname, roomnum):
    print(firstname, lastname)
    print(f"Room #{roomnum}")
    print("Kookmin Univ., South Korea")

printMyAddress("Mingi", "Kweon", 209)


def get_sum(first,second,*list):
    print(first)
    print(second)
    print(list)

print(get_sum(2,3,4))
print()
print()
print()

get_sum(1,2,5,6,7,8,9,20)

def testf(n = 1):
    n += 3
    return n

print(testf(17))


def test(n = 2):
    n += 4
    return print(n) , n

print()
test(54)


print()
print()
print()
print()
print()



def cal(price, tax_rate):
    total = price + (price * tax_rate)
    print(my_price)
    return total

my_price = float(input("Enter a price: "))

totalPrice = cal(my_price, 0.06)
print("price = ", my_price, "Total price = ", totalPrice)