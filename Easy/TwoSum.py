# This solution uses a hash-map (a Dict in python) to solve the two-sum problem

class Solution(object):
    def twoSum(self, nums, target):

        Dict = {}

        for i in range((len(nums))):

            remaining = target - nums[i]

            if remaining in Dict:
                return [Dict[remaining], i]
            else:
                Dict[nums[i]] = i
            
if __name__ == "__main__":
    

    s1 = Solution()
    testList = [2,7,11,15]
    indices = s1.twoSum(testList, 17)

    print(indices)

    #while node:
    #    print(node.val)
    #    node = node.next