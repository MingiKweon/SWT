import sys
n , m = map(int, sys.stdin.readline().split())


studentId = {}
for i in range(m):
    x = sys.stdin.readline().rstrip()
    studentId.update({x:i+1})

student3 = sorted(studentId, key = lambda x : x[1])
print(student3[:n])
# for j in student3[:3]:
#     print(j)