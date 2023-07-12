num_list = [1,2,3]

for i in num_list:
    print("Hello", end="\n")
    print("Your number is", i, ".") 
    print(f"Your number is {i}.") #f-string
    print("Your number is {}.".format(i)) #f-string
    print("Your number is %d.") #이거 다시..
print("Done!")