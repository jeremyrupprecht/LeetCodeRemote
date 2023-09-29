# 15 3Sum
# https://leetcode.com/problems/3sum/

def threeSum(nums):

    nums.sort() # nlogn
    output = []
    p1 = 0
    p2 = 1
    p3 = len(nums) - 1

    for p1 in range(len(nums)):                 #n time --> use dominant term --> nlogn
        total = nums[p1] + nums[p2] + nums[p3]
        if total == 0:
            output.append([nums[p1], nums[p2], nums[p3]])

    return output

if __name__ == "__main__":

    nums = [-1,0,1,2,-1,-4]
    print(threeSum(nums))
    