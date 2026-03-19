# sum of 1+x^1+x^2+.....n

x = int(input("Enter value of x: "))
sum = 1 + x + x**2
print("Sum =", sum)


# sum of 1+x^1/1+x^2/2+x^3/3+.....n

x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))
sum = 1
for i in range(1, n+1):
    sum = sum + (x**i)/i
print("Sum =", sum)

# nested for loop

for i in range(4):        # outer loop (rows)
    for j in range(4):    # inner loop (columns)
        print(1, end="")
    print()


# nested for loop ex:\

for i in range(1, 5):        # rows
    for j in range(i):       # stars in each row
        print("*", end="")
    print()

# nested for loop:

for i in range(1, 5):
    for j in range(i):
        print(chr(97 + j), end=" ")
    print()
