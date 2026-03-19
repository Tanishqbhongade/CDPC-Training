# Roy wants to change his profile picture on Facebook. Now Facebook has some restriction over the dimension of picture that we can upload.
# Minimum dimension of the picture can be L x L, where L is the length of the side of square.

L = int(input())
N = int(input())
for _ in range(N):
    W, H = map(int, input().split())
    if W < L or H < L:
        print("UPLOAD ANOTHER")
    elif W == H:
        print("ACCEPTED")
    else:
        print("CROP IT")


# Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K , where she needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new to the school, please help her to complete the task.

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    K = K % N
    rotated = A[-K:] + A[:-K]
    print(*rotated)


# You have been given a String S consisting of uppercase and lowercase English alphabets. You need to change the case of each alphabet in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. You need to then print the resultant String to output.

S = input()
result = ""
for ch in S:
    if ch.islower():
        result += ch.upper()
    else:
        result += ch.lower()
print(result)


# find the majority of the element that appeaers more than n/2 times in an array.

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
n = len(arr)
for i in arr:
    count = arr.count(i)
    if count > n // 2:
        print("Majority Element:", i)
        break


# product of an array exept itself return an array where each element is the product of all elemrnts in the array except itself use two passes one from left to right and one from right to left to calculate product

arr = [1, 2, 3, 4]
n = len(arr)
result = [1] * n

left = 1
for i in range(n):
    result[i] = left
    left *= arr[i]
right = 1
for i in range(n - 1, -1, -1):
    result[i] *= right
    right *= arr[i]
print(result)
