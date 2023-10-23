# 704. Binary Search
# https://leetcode.com/problems/binary-search/
# O(logn) --> O(nlogn) if you have to sort the array
# This question assumes that the input array is sorted

def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:     # found the target
            return mid
        elif nums[mid] < target:    # target is above the midpoint, check top half of array
            l = mid + 1
        else:                       # target is below the midpoint, check bottom half of array
            r = mid - 1         
    return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 2
    print(search(nums, target))