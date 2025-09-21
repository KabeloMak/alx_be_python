number = int(input("Enter the size of the pattern: "))

if number < 0:
    print("Enter positive number")

if number >= 1:
    row = 0
    while row < number:
        for _ in range(number):
            print("*", end ="")
        print()
        row += 1