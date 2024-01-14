# 15. 3Sum
# https://leetcode.com/problems/3sum/description/
def threeSum(nums):
    outputSet = set()
    outputList = []
    nums.sort()
    for i in range(len(nums)-2):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            result = nums[i] + nums[l] + nums[r]
            if result == 0:
                resultSet = frozenset({nums[i], nums[l], nums[r]})
                if resultSet not in outputSet:
                    outputSet.add(resultSet)
                    outputList.append([nums[i], nums[l], nums[r]])
                l += 1
            elif result < 0:
                l += 1
            else:
                r -= 1
    return outputList
            
if __name__ == "__main__":

    nums = [-1,0,1,2,-1,-4]
    nums2 = [0,1,1]
    nums3 = []
    nums4 = [7,7,7,7,7,7,7,7,-1,0,1,7,7,7,7,1,0,-1]
    print(threeSum(nums4))