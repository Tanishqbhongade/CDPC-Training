# 1st code two sum

class solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    output.append(i)
                    output.append(j)
                    return output


# Fizz Buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for i in range(1,n+1):
            if(i%5==0 and i%3==0):
                answer.append("FizzBuzz")
            elif(i%5==0):
                answer.append("Buzz")
            elif(i%3==0):
                answer.append("Fizz")
            else:
                answer.append(str(i))
        return answer


# Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums


# In the array the next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4 since it doesnt exist, it is -1

arr = [1,3,2,4]
n = len(arr)
output=[]
for i in range(n):
    for j in range(i+1,n):
        if (arr[j]>arr[i]):
            output.append(arr[j])
            break
    else:
        output.append(-1)
print(output)
