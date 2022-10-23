# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1



def runningSum(nums):
        
    nums = [1,2,3,4]

    returnList = []
        
    for i in range(0, len(nums)):
            
        count = 0
            
        for o in range(0, i + 1):

            count += nums[o]
            
        returnList.append(count)
            
    print(returnList)

if __name__ == '__main__':
    a = []
    runningSum(a)
