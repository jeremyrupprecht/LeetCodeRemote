# 1343 Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

def numOfSubarrays(arr, k, threshold):
    from statistics import mean 
    runningSum = 0
    numberOfSubarrays = 0
    l = 0
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