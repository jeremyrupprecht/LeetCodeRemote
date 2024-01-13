# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/

def longestConsecutive(nums):
    numsSet = set(nums)
    longest = 0
    for n in nums:
        if (n - 1 not in numsSet):
            currentLongest = 1
            while (n + 1 in numsSet):
                n += 1
                currentLongest += 1
            longest = max(currentLongest, longest)
    return longest

if __name__ == "__main__":

    nums = [100,4,200,1,3,2]
    nums2 = [0,3,7,2,5,8,4,6,0,1]
    nums3 = [1,1,1,1,1,1,1,1,2,3,4]
    nums4 = [1,2,0,1]
    nums5 = []
    nums6 = [0,0,0,0,0,0]
    nums7 = [0,0,1,-1]
    print(longestConsecutive(nums3))