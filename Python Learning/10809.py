x = input()

pos = 0
num_list = []

for i in range(97,123):
    for j in x:
        if chr(i) != j:
            pos += 1
            if chr(i) == j:
                num_list.append(pos)
                pos = 0
                break
            elif pos == len(x):
                pos = -1
                num_list.append(pos)
                pos = 0
                break
        else:
            num_list.append(pos)
            pos = 0 
            break

for w in num_list:
    print(w , end=" ")