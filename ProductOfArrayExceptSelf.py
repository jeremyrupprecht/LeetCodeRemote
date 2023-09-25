# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

"""
# Intuition 
<!-- Describe your first thoughts on how to solve this problem. -->

    brute force --> double loop, loop through the list, 
    for each element, loop through the list and calculate
    the product of the rest of the elements in the list
    and store that at the correct spot in the return array
    --> n^2 time

# Approach
<!-- Describe your approach to solving the problem. -->

    Problem-solving/Proposed-solution/Pseudocode

    -make two passes over the input array, calculate prefix products on 1st, 
     postfix products on 2nd, onto a single output array

     -pseudocode:
        -create prefix variable = 1
        -loop 1:
            -put prefix in output spot of return array
            -multiply current input # by prefix to get the new prefix
            -move to the next input #
        
        -loop 2:
            -put postfix in output spot of return array
            -multiply current input # by postfix to get the new postfix
            -move to the next input #
        -return return array

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

    2 passes over n array --> O(n) + O(n) = 2O(n) -> O(n)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

    not counting the output array (as stated in the question)
    --> O(n) space 
"""

def productExceptSelf(nums):
    output = [1] * len(nums)
    prefix = 1
    postfix = 1
    # prefix loop
    for i in range(len(nums)):
        output[i] = prefix
        prefix *= nums[i]
    # postfix loop
    for i in range(len(nums)-1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]                    
    return output

if __name__ == "__main__":

    nums = [1,2,3,4]
    print(productExceptSelf(nums))
