# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(nums):

    output = [1] * len(nums)
    runningProduct = 1
    for i in range(len(nums)):
        if i != 0:
            runningProduct *= nums[i-1]
            output[i] = runningProduct

    runningProduct = nums[len(nums)-1]
    for i in range(len(nums)-2,-1,-1):
        output[i] *= runningProduct
        runningProduct *= nums[i]

    return output

if __name__ == "__main__":
    nums = [1,2,3,4]
    nums2 = [-1,1,0,-3,3]
    print(productExceptSelf(nums2))