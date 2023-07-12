book = {}

n = int(input())
for i in range(n):
    m = input()
    if m in book:
        book[m] += 1
    else:
        book[m] = 1

count = 0
book_lst = dict(sorted(book.items()))
for j in book_lst:
    if book_lst[j] > count:
        count = book_lst[j]
        biggest = j
print(biggest)
