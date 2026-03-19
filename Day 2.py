# if the sum of factorials of each digit is equal to the sum of suppose we have to check the number

import math
num = int(input("Enter a number: "))
temp = num
sum_fact = 0
while temp > 0:
    digit = temp % 10
    sum_fact += math.factorial(digit)
    temp //= 10
if sum_fact == num:
    print("It is a Factorion number")
else:
    print("It is not a Factorion number")


# reverse a no. using loop

n = int(input("Enter a number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reversed number:", rev)


# count the no. of digits

n = int(input("Enter a number: "))
count = 0

while n > 0:
    n = n // 10
    count = count + 1
print("Number of digits:", count)


# sum of digits

n = int(input("Enter a number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print("Sum of digits:", sum)

# check the no. is palindrome or not

n = int(input("Enter a number: "))
temp = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if rev == temp:
    print("Palindrome number")
else:
    print("Not a palindrome number")


# no. to check is armstrong

num = int(input("Enter a number: "))
temp = num
sum = 0
n = len(str(num))
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** n
    temp = temp // 10
if sum == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")


# no. 1 to 1000 find armstrong no

for num in range(1, 1001):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp //
    if sum == num:
        print(num)
