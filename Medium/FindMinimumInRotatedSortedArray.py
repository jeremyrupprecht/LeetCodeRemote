# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def findMin(nums):
    # cover base case and arrays w/ no rotations (array is fully sorted, first
    # element is the smallest )
    if len(nums) < 2 or nums[len(nums)-1] > nums[0]:   
        return nums[0]
    # Use Binary search to find the pivot point
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        # the pivot point is the only point in the array with a
        # non-increasing set of two elements, since this is the 
        # only point, this has to be the point with the smallest 
        # element

        # found pivot point
        if nums[mid] < nums[mid - 1]:           # 4,5, --> 0 <-- ,1,2,3
            return nums[mid]
        elif nums[mid] > nums[mid + 1]:         # 3,4, --> 5 <-- ,0,1,2  
            return nums[mid+1]
            
        if nums[mid] > nums[r]:
            # in rotated section
            l = mid + 1
        else:
            # in non-rotated section
            r = mid - 1

if __name__ == "__main__":
    nums = [3,4,5,1,2]
    nums2 = [4,5,6,7,0,1,2]
    nums3 = [11,13,15,17]
    nums4 = [10,0,1,2,3,4,5,6,7,8,9]
    nums5 = [17]
    print(findMin(nums5))