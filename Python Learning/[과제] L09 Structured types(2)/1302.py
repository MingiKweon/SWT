n = int(input())

book = []

for i in range(n):
    m = input()
    book.append(m)

book_lst = sorted(list(set(book)))


num_lst = []
for k in book_lst:
    num = 0
    while k in book:
        num += 1
        book.remove(k)
        num_lst.append(num)


#다시 고칠 것..