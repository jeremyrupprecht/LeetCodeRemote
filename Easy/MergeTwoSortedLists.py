# Definition for singly-linked list.

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # create a dummy node (to use as a temporary node)

        dummy = ListNode()
        tail = dummy

        # loop through the list, if a node in list1 is 
        # less than a node in list2, then make the dummy
        # node point to it
        #
        #   if L1 < L2:
        #
        #       TAIL -> L1
        #
        #   else: (L1 >= L2):
        #
        #       TAIL -> L2
        #   
        #   then update the current node:
        # 
        #   TAIL -> L1 or L2
        #   
        #   becomes:
        #
        #   L1 or L2 -> nothing

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # update the current node

            tail = tail.next        # THIS IS EITHER LIST1 OR LIST 2

        # if either 
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2


        return dummy.next

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