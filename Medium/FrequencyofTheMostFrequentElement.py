
# 1838 Frequency of the Most Frequent Element
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

def maxFrequency(nums, k):
    # sort the array because: tldr: it uncomplicates things A LOT, 
    # worth going to O(nlogn)
    #
    # we want to increment smaller values into larger ones --> sorting 
    # prevents having to hold a max value and increment values that 
    # aren't at R (up to R) --> also prevents having to use a dictionary
    # and incrementing values (that are higher than whats at R) up
    # to the highest value (searching the dict for the highest value
    # and then incrmenting all other values while decrementing k
    # might take longer than O(nlogn))
    nums.sort()
    l = 0
    longestWindow = 0
    windowTotal = 0
    for r in range(len(nums)):
        windowTotal += nums[r]
        # want to expand the window until the sum of 
        # the fully incremented elements in the window 
        # is greater than the sum of the normal elements 
        # in the window plus k --> we want to keep expanding
        # the window (moving R) as much as possible while still
        # staying under the k "budget" (without exceeding k),
        # once the total of fully incremented elements exceeds
        # the total + k, move L (shift the window) to bring the 
        # budget back under k (saving the max allowed window 
        # size as you go along)
        while (nums[r] * (r - l + 1) > windowTotal + k):
            windowTotal -= nums[l]
            l += 1
        longestWindow = max(longestWindow, (r - l + 1))
    return longestWindow


if __name__ == "__main__":
    
    nums = [1,2,4]
    k = 5
    nums2 = [1,2,1,1,2,3,4]
    nums3 = [1,4,8,13]
    nums4 = []
    nums5 = [3,9,6]
    print(maxFrequency(nums4, 2))

