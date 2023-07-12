x,n,m = map(int,input().split())

#print("000000000000000000000000000"+bin(x)[2:])
#print("0"*31+bin(x)[2:])

binstring = ("0"*31)+bin(x)[2:]
l = len(binstring)

print(binstring[l-m-1:l-n])