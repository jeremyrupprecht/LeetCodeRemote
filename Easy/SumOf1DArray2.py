# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1

def runningSum(nums):
        
    nums = [3,1,2,10,1]

    returnList = [nums[0]]
    runningCount = nums[0]

    for i in range(1, len(nums)):
        runningCount += nums[i]
        returnList.append(runningCount)

    print(returnList)

if __name__ == '__main__':
    a = []
    runningSum(a)
