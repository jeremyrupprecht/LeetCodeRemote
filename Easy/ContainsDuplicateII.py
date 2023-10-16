# 219 Contains Duplicate II 
# https://leetcode.com/problems/contains-duplicate-ii/

def containsNearbyDuplicate(nums, k):
    Dict = {}
    l = 0
    for r in range(len(nums)):
        Dict[nums[r]] = Dict.get(nums[r], 0) + 1
        # if window is too big, move l (resize window to be equal to k)
        if (r - l) > k:
            if nums[l] in Dict:
                if Dict[nums[l]] > 1:
                    Dict[nums[l]] -= 1
                else:
                    Dict.pop(nums[l])
            l += 1
        # check dict for dups --> if any value is 2 (a dup is found)
        if Dict[nums[r]] >= 2:
            return True
    return False


if __name__ == '__main__':
    nums = [1,2,3,1]
    k = 3
    nums2 = [1,0,1,1]
    k1 = 1
    nums3 = [1,2,3,1,2,3]
    k2 = 2
    nums4 = [1,0,1,1]
    k3 = 1
    print(containsNearbyDuplicate(nums4, k3))