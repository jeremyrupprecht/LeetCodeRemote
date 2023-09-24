# 347 Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

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
         in the dictionary as such: element:number-of-occurrences, 
        -grab key with the maximum value in the Dict
        -pop that value out of the dict
        -place the value in the return list
        -repeat k times
        -return the return list

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->


"""

def topKFrequent(nums, k):

    returnList = []
    Dict = {}
    for number in nums:
        if number in Dict:
            Dict[number] = Dict[number] + 1
        else:
            Dict[number] = 1

    for i in range(k):
        maxValue = max(Dict, key=Dict.get)
        Dict.pop(maxValue)
        returnList.append(maxValue)

    return returnList

if __name__ == "__main__":

    nums = [1]
    k = 1
    #topKFrequent(nums, k)
    print(topKFrequent(nums, k))