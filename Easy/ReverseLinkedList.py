# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # To reverse a linked list, simply make every node
        # point to it's previous node, to do this with
        # a linked list use 3 variables:
        #
        #   prev: to hold the previous node of the current node
        #
        #   current: to hold the current node
        #
        #   next: to hold the next node of the current node
        #
        # The algorithm is as follows:
        #
        # wihle the current node is not NULL (not at the end of the list)
        # 1. update next
        # 2. make current point to prev
        # 3. update current
        # 4. update next
        
        current = head
        prev = None
        
        while current:

            # 1.
            next = current.next

            # 2.
            current.next = prev

            # 3.
            prev = current

            # 4.
            current = next


        return prev

    def test(self, head):
        while head:
            print(head.val)
            head = head.next

if __name__ == "__main__":
    
    list = []
    one = ListNode(1)
    list.append(one)
    two = ListNode(2)
    list.append(two)
    one.next = two
    three = ListNode(3)
    list.append(three)    
    two.next = three
    four = ListNode(4)
    list.append(four)
    three.next = four
    five = ListNode(5)
    list.append(five)
    four.next = five

    s1 = Solution()
    node = s1.reverseList(one)

    while node:
        print(node.val)
        node = node.next
