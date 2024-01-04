# 1. Two Sum
# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    Dict = {}
    for i in range(len(nums)):
        if (target - nums[i]) in Dict.keys():
            return [i, Dict[target-nums[i]]]
        else:
            Dict[nums[i]] = i

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9

    nums2 = [3,2,4]
    target2 = 6

    nums3 = [3,3]
    target3 = 6

    nums4 = [3,3,3,3,3,3,3,3,3,10,7]
    target4 = 17

    print(twoSum(nums4, target4))
