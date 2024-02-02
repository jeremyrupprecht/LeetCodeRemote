# https://leetcode.com/problems/add-two-numbers/
# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        str1 = ""
        str2 = ""
        while l1 or l2:
            if l1:
                str1 = str(l1.val) + str1
                l1 = l1.next
            if l2:
                str2 = str(l2.val) + str2
                l2 = l2.next
        
        result = str(int(str1) + int(str2))
        numNodes = len(result)
        head = ListNode(0)
        current = head
        while numNodes > 0:
            new = ListNode(int(result[-1]))
            result = result[:-1]
            current.next = new
            current = new
            numNodes -= 1

        return head.next
