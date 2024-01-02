# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    hashSet = set()
    for n in nums:
        if n in hashSet:
            return True
        else:
            hashSet.add(n)
    return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    nums2 = [1,2,3,4]
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    nums4 = []
    nums5 = [10,2,3,4,5,6,7,8,9,10]
    print(containsDuplicate(nums5))
