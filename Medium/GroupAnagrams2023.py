# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams

"""
# Intuition 
<!-- Describe your first thoughts on how to solve this problem. -->

    brute --> loop over the input array, for the first string, 
    remove it from the array, put it into a new array
    and then loop/scan over the input array for anagrams, 
    once an anagram is found, remove it from the array 
    and into the list of the matching anagram --> do this
    for the rest of the strings in the input array

# Approach
<!-- Describe your approach to solving the problem. -->

    Problem Solving:

    1. Understand question in english --> given a 1d array of strings, group together 
       all of the anagrams into arrays witin the 1d array (to create 2d array where 
       each group is made of anagrams of each other)

    2. Questions
        UI:          text-based
        Inputs:      a 1d array of strings that are anagrams 
        Outputs:     a 2d array of strings with the anagrams grouped together       
    
    3. Proposed solution/Pseudocode

    -Use a dictionary 
    -loop over the input array, for each string/element: 
    -sort the string's characters
        -if it's not in the dictionary --> store it as such: sortedString:originalString 
        -if it IS in the diciontary --> append the string to the dictionary value as such: sortedString:anagramString, originalString
    -return the dictionary values as an array (each value is also also an array, creating 
    the 2d array return type required by the question)

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

    numberOfElementsOrn * time to store each one in the Dict * time to sort each element?

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

    O(2n) -> O(n)?

"""

def groupAnagrams(strs):
    
    Dict = {}

    for string in strs:
        sortedString = "".join(sorted(string))
        if sortedString in Dict:
            Dict[sortedString].append(string)
        else:
            Dict[sortedString] = [string]
            
    return Dict.values()

if __name__ == '__main__':
    a = ["eat","tea","tan","ate","nat","bat"]
    b = [""]
    result = groupAnagrams(b)
    print(result)

