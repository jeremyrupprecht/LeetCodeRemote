# 1343 Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

def numOfSubarrays(arr, k, threshold):
    runningSum = 0
    numberOfSubarrays = 0
    l = 0
    # mean = runningSum / k where runningSum is the sum of 
    # the current window, when the window slides (r and l move)
    # the running Sum is updated accordingly 
    for r in range(len(arr)):
        runningSum += arr[r]
        if (r - l) >= k:
            runningSum -= arr[l]
            l += 1
        if (r - l + 1) == k and (runningSum / k) >= threshold:
            numberOfSubarrays += 1
    return numberOfSubarrays

if __name__ == "__main__":

    arr = [2,2,2,2,5,5,5,8]
    k = 3
    threshold = 4
    print(numOfSubarrays(arr, k, threshold))