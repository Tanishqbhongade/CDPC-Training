# hackerrank questions 7704

def compareTriplets(a, b):
    alice = 0
    bob = 0

    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1

    return [alice, bob]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = compareTriplets(a, b)
print(result[0], result[1])


# hackerrank questions 7702  Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    n = len(arr)
    primary = 0
    secondary = 0

    for i in range(n):
        primary += arr[i][i]
        secondary += arr[i][n - i - 1]

    return abs(primary - secondary)

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
print(diagonalDifference(arr))


# Given an array of integers, calculate the ratios of its elements that are , positive , negative and zero . Print the decimal value of each fraction on a new line with 6 places after the decimal.

def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zero = 0

    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1

    print(f"{pos / n:.6f}")
    print(f"{neg / n:.6f}")
    print(f"{zero / n:.6f}")

n = int(input())
arr = list(map(int, input().split()))
plusMinus(arr)


# array rotation. rotate an array to the right by a given no. of steps:

def rotate_right(arr, k):
    n = len(arr)
    k = k % n   # handle cases where k > n
    rotated = arr[-k:] + arr[:-k]
    return rotated

arr = [1, 2, 3, 4, 5]
k = 2

print(rotate_right(arr, k))
