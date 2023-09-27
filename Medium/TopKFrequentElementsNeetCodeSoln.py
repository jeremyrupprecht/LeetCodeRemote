# 347 Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# https://www.youtube.com/watch?v=YPTqKIgVk-k

"""
# Intuition 
<!-- Describe your first thoughts on how to solve this problem. -->

    brute force --> ...

# Approach
<!-- Describe your approach to solving the problem. -->

    Problem Solving:

    1. Understand question in english --> given an array and an integer k, return 
       the k most frequently occuring elements, if k = 3, the most frequently occuring
       3 elements are returned

    2. Questions
        UI:          text-based
        Inputs:      an array and an integer k
        Outputs:     an array of the most frequently occuring elements
    
    3. Proposed solution/Pseudocode

        -use a hash map (a dictionary in python), store each element in the input array 
        in the dictionary as such: element:number-of-occurrences, then use an array where
        the index of the array is how many occurences of each element, and the element 
        is stored (in an array) at that index --> see the neetcode video for more details

        -return the return list

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

    O(n) to store each element in the Dict
    +
    O(n) to store each element in the bucket array
    +
    K to loop over the array K times to return the top K elements
    =
    O(n) + O(n) + k --> O(n) time

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

    O(n) Dict
    + 
    O(n) bucket array 
    -> O(n) time


"""

def topKFrequent(nums, k):

    returnList = []
    bucketList = [0] * (len(nums) + 1)
    Dict = {}
    for number in nums:
        if number in Dict:
            Dict[number] = Dict[number] + 1
        else:
            Dict[number] = 1

    for key, value in Dict.items():
        if bucketList[value] == 0:
            bucketList[value] = [key]
        else:
            bucketList[value].append(key)

    length = len(nums)
    while length > 0 and k > 0:
        if bucketList[length] != 0:
            for item in bucketList[length]:
                returnList.append(item)
                k -= 1
        length -= 1

    return returnList

if __name__ == "__main__":

    nums = [4,1,-1,2,-1,2,3]
    k = 2
    #output: [-2,1]
    print(topKFrequent(nums, k))