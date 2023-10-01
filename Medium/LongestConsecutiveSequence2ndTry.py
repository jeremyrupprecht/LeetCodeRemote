def longestConsecutive(nums):
    numsSet = set(nums)                     # O(n) time
    longestSeq = 0  
    for i in range(len(nums)):              # O(n) time
        if nums[i] - 1 not in numsSet:
            currentSeq = 1
            while nums[i] + 1 in numsSet:
                currentSeq += 1
                nums[i] += 1
            longestSeq = max(currentSeq, longestSeq)
    return longestSeq

if __name__ == "__main__":

    nums = [100,4,200,1,3,2]
    nums2 = [100, 200, 0, 1, 2]
    nums3 = [4,3,2,5]
    nums4 = [0,3,7,2,5,8,4,6,0,1]
    result = longestConsecutive(nums)
    print(result)