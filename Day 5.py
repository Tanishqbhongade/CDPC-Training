#find maximum and minimum elements. write a function to find the maximum and minimum elements in array

def find_max_min(arr):
    maximum = max(arr)
    minimum = min(arr)
    return maximum, minimum

arr = [5, 3, 9, 2, 8]

max_val, min_val = find_max_min(arr)

print("Maximum element:", max_val)
print("Minimum element:", min_val)


# remopve duplicates from unsirted array write a function to remove duplicate from an unsorted array.

def remove_duplicates(arr):
    unique = list(set(arr))
    return unique


arr = [3, 2, 3, 1, 2, 4]

result = remove_duplicates(arr)

print("Array after removing duplicates:", result)


# use of in operator

numbers = [1, 2, 3, 4, 5]
print(5 in numbers)


# use of not in operator

numbers = [1, 2, 3, 4, 5]
print(7 not in numbers)

# remopve duplicates from unsirted array write a function to remove duplicate from an unsorted array. using of not in operator

def remove_duplicates(arr):
    unique = []

    for num in arr:
        if num not in unique:
            unique.append(num)

    return unique


arr = [4, 2, 7, 2, 9, 4, 1]

result = remove_duplicates(arr)

print("Array after removing duplicates:", result)


# use of break statement

for i in range(1, 6):
    if i == 4:
        break
    print(i)


# use of continue statement

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# solve this pattern with continue statement

n = 10
for i in range(1, n//2 + 1):
    if i == 3:
        continue
    print(i, n - i + 1)


# rearrange the positive and negative no. given an array containing both positive and negative no. rearrange them in an alternating fasion
