# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
def longestConsecutive(nums):
    nSet = set(nums)
    longest = 0
    for n in nums:
        if (n - 1 not in nSet):
            largestSeq = 1
            while (n + largestSeq in nSet):
                largestSeq += 1
            longest = max(longest, largestSeq)
    return longest
            
if __name__ == "__main__":

    nums = [100,4,200,1,3,2]
    nums2 = [100, 200, 0, 1, 2]
    nums3 = [4,3,2,5]
    nums4 = [0,3,7,2,5,8,4,6,0,1]
    result = longestConsecutive(nums4)
    print(result)