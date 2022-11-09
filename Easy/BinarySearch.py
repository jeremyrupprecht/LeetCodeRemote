# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution(object):
    def search(self, nums, target):

        lower = 0
        higher = len(nums) -1

        while lower <= higher:

            middle = (higher + lower) // 2

            if nums[middle] == target:
                return middle
            elif (nums[middle] < target):
                lower = middle + 1
            elif (nums[middle] > target):
                higher = middle - 1
                
        return -1


if __name__ == "__main__":

    nums = [-1,0,3,5,9,13]
    target = 9
    s1 = Solution()
    print(s1.search(nums, target))

