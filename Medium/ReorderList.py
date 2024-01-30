# 143. Reorder List
# https://leetcode.com/problems/reorder-list/description/

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def reorderList(self, head):
        copyArr = []
        current = head
        while current:
            copyArr.append(current)
            current = current.next

        left = 0
        right = len(copyArr) - 1
        while left < right:
            temp = head.next
            head.next = copyArr[right]
            head = temp
            left += 1

            if left == right:
                break
            
            copyArr[right].next = head
            right -= 1
        
        head.next = None
        copyArr[right].next = None

if __name__ == "__main__":

    # Create the nodelist
    nodes = ListNode(1)
    nodesHead = nodes
    numberOfNodes = 7
    for i in range(2, numberOfNodes):
        node = ListNode(i)
        nodes.next = node
        nodes = nodes.next

    s1 = Solution()
    s1.reorderList(nodesHead)

    while (True):
        print(nodesHead.val)

        if nodesHead.next == None:
            break
        
        nodesHead = nodesHead.next