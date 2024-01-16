# 15 3Sum
# https://leetcode.com/problems/3sum/

def threeSum(nums):
    # sort the list for the two pointers alg to work
    nums.sort()
    output = []
    p1 = 0
    for p1 in range(len(nums)):
        # check for and skip duplicates
        # put not on the first iteration --> p1 > 0
        # as the first iteration may include the 
        # matching combo of numbers --> ex: [[0,0,0]]
        if p1 > 0 and nums[p1] == nums[p1-1]:
            continue
        # Two Pointers alg
        p2 = p1 + 1
        p3 = len(nums) - 1
        while p2 < p3:
            total = nums[p1] + nums[p2] + nums[p3]
            if total == 0:
                output.append([nums[p1], nums[p2], nums[p3]])
                # if the total is found, move one of the pointers, and skip 
                # duplicates when doing so --> don't have to check for duplicates
                # for both pointers --> as once a non-duplicate value is found 
                # with moving pointer, the "total" value will have changed
                # and a new 3 number pair will be created anyways, so only moving 
                # one pointer is sufficient
                p2 += 1
                print(p1, p2, p3, nums[p1], nums[p2], nums[p3])
                while nums[p2] == nums[p2-1] and p2 < p3:
                    p2 += 1
            # conditionally change the total
            elif total < 0:
                p2 += 1
            else:
                p3 -= 1
    return output

if __name__ == "__main__":

    nums = [-1,0,1,2,-1,-4]
    nums2 = [-3,3,4,-3,1,2,1,1,1,1,-3,3,4,-3,1,2]
    print(threeSum(nums2))
    