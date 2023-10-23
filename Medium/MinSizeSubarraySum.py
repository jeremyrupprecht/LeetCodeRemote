# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

def minSubArrayLen(target, nums):
    import sys
    currentMin = sys.maxsize
    minLength = sys.maxsize
    wTotal = 0
    l = 0
    for r in range(len(nums)):
        wTotal += nums[r]

        if wTotal >= target:
            currentMin = r - l + 1

        while (wTotal - nums[l]) >= target:
            wTotal -= nums[l]
            l += 1
            currentMin = r - l + 1

        minLength = min(minLength, currentMin)

    if minLength == sys.maxsize:
        return 0
    else:
        return minLength
 

if __name__ == "__main__":
    nums = [2,3,1,2,4,3]
    nums1 = [1,1,1,1,1,1,1,1]
    nums2 = [1,4,4]
    print(minSubArrayLen(4, nums2))
