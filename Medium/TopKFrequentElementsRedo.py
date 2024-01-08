# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent(nums, k):
    Dict = {}
    highestFrequencyCount = -1
    for i in range(len(nums)):
        if nums[i] in Dict:
            Dict[nums[i]] += 1
        else:
            Dict[nums[i]] = 1
        highestFrequencyCount = max(highestFrequencyCount, Dict[nums[i]])

    bucketSortList = [[]] * (highestFrequencyCount + 1)
    for key in Dict:
        if bucketSortList[Dict[key]]:
            bucketSortList[Dict[key]].append(key)
        else:
            bucketSortList[Dict[key]] = [key]

    mostFrequentElements = []
    endOfBucketSortList = len(bucketSortList) - 1
    print(endOfBucketSortList)
    while (k > 0 and endOfBucketSortList > 0):

        if not bucketSortList[endOfBucketSortList]:
            endOfBucketSortList -= 1
            continue

        for n in bucketSortList[endOfBucketSortList]:
            mostFrequentElements.append(n)
            k -= 1

        endOfBucketSortList -= 1

    return mostFrequentElements

if __name__ == "__main__":
    nums = [1,1,1,1,1,1,1,2,2,3]
    nums2 = [1,2,1]
    nums3 = [3,0,1,0]
    nums4 = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
    print(topKFrequent(nums4,10))
