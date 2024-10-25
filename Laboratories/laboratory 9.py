rows = int(input("Enter Number of Rows: "))
i = 1

for x in range(1, rows+1):
    for y in range(1, x+1):
        print(i, end=" ")
        i += 1
    print()