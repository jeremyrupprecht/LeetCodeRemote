# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        outputHead = None
        outputCurrent = None
        while (list1 or list2):
            temp = None

            if (list1 and not list2) or ((list1 and list2) and list1.val <= list2.val):
                temp = list1
                list1 = list1.next
            elif (not list1 and list2) or ((list1 and list2) and list1.val > list2.val):
                temp = list2
                list2 = list2.next
        
            if not outputHead:
                outputHead = temp
                outputCurrent = temp
            else:
                outputCurrent.next = temp
                outputCurrent = temp

        return outputHead
      
if __name__ == "__main__":

    list1 = ListNode(1)
    node1 = ListNode(2)
    list1.next = node1
    node2 = ListNode(4)
    node1.next = node2

    list2 = ListNode(1)
    node3 = ListNode(3)
    list2.next = node3
    node4 = ListNode(4)
    node3.next = node4

    s1 = Solution()
    #print(Solution.mergeTwoLists(Solution, list1, list2))
    current = s1.mergeTwoLists(list1, list2)

    while (True):
        print(current.val)

        if current.next == None:
            break
        
        current = current.next