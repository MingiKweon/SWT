import sys

a , b = map(int,sys.stdin.readline().split())

student = {}
for i in range(b):
    x = sys.stdin.readline().rstrip()
    student.update({x:i+1})

for j in dict((sorted(student.items(), key = lambda x : x[1]))[:a]):
    print(j)