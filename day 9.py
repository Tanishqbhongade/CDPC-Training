# palindrome number

def isPalindrome(x: int) -> bool:
    # Negative numbers and numbers ending with 0 (except 0) are not palindrome
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0

    # Reverse half of the number
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # Check for even and odd length
    return x == reversed_half or x == reversed_half // 10


# Richest Customer Wealth






# You have been given an array A of size N consisting of positive integers. You need to find and print the product of all the number in this array Modulo

def productOfArray(arr):
    MOD = 10**9 + 7
    result = 1
    for num in arr:
        result = (result * num) % MOD
    return result
N = int(input())
arr = list(map(int, input().split()))
print(productOfArray(arr))


# staircase (n=4)

def staircase(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        hashes = "#" * i
        print(spaces + hashes)
n = int(input())
staircase(n)


# Mini-Max Sum

def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[:4])  # first 4 elements
    max_sum = sum(arr[1:])  # last 4 elements
    print(min_sum, max_sum)
arr = list(map(int, input().split()))
miniMaxSum(arr)


# Birthday Cake Candles

def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = candles.count(tallest)
    return count
n = int(input())
candles = list(map(int, input().split()))
print(birthdayCakeCandles(candles))


# Time Conversion

def timeConversion(s):
    period = s[-2:]          # AM or PM
    hour = int(s[:2])
    rest = s[2:-2]           # :mm:ss

    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    return f"{hour:02d}{rest}"
s = input()
print(timeConversion(s))


#
