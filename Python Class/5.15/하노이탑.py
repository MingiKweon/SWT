def hanoi(start, end, middle, n):
    if n == 1:
        print(f"{start} -> {end}")
    else:
        hanoi(start, middle, end , n-1)
        hanoi(start, end, middle , 1)
        hanoi(middle, end, start , 1)

