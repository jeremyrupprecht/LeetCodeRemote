# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l < r:
        currentTarget = numbers[l] + numbers[r]
        if currentTarget == target:
            return [l + 1, r + 1]
        elif currentTarget < target:
            l += 1
        else:
            r -= 1
    return []


if __name__ == "__main__":

    nums = [2,7,11,15]
    nums2 = [2,3,4]
    nums3 = [-1,0]
    nums4 = [1,2,3,5,10,11]
    print(twoSum(nums4, 15))