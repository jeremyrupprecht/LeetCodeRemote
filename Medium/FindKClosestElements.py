# 658. Find K Closest Elements
# https://leetcode.com/problems/find-k-closest-elements/

# This was solved using the Two Pointers algorithm, this problem can also be
# solved using a Sliding Window (probably), and using a non-intuitive version
# of Binary Search (see the Neetcode video for this...)

def findClosestElements(arr, k, x):
    l = 0
    r = len(arr) - 1
    while (r - l + 1) > k:
        if abs(arr[r] - x) >= abs(arr[l] - x):
            r -= 1
        else:
            l += 1

    return arr[l:r+1]

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    arr2 = [1,2,3,3,10,11,12,12,12,15,16,27]
    arr3 = [1,2,3,3,10,11,12,12,13,13,13,13]
    print(findClosestElements(arr3,4,13))