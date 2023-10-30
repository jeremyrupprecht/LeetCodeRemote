# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):
    rotationPt = nums[len(nums) - 1]
    targetInRotated = False
    if target > rotationPt:
        targetInRotated = True
    
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > rotationPt:
            # in rotated
            if targetInRotated:         # and we want to be in rotated
                if nums[mid] < target:  # it becomes a normal binary search
                    l = mid + 1
                else:
                    r = mid - 1
            else:                       # in rotated, and don't want to be there,
                l = mid + 1             # navigate to non-rotated
        else:
            # in non-rotated 
            if targetInRotated:         # in non-rotated and don't want to be here
                r = mid - 1             # navigate to rotated
            else:                       
                if nums[mid] < target:  # and we want to be here
                    l = mid + 1         # it becomes a normal binary search
                else:
                    r = mid - 1
    return -1

if __name__ == "__main__":

    nums = [4,5,6,7,0,1,2]
    nums2 = [4,5,6,7,8,9,10,11,12,13,14,15,1,2,3]
    nums3 = [0,1,2,3,4,5,6,7,8,9]
    print(search(nums3, 9))