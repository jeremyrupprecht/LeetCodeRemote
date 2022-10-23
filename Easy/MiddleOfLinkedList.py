# Definition for singly-linked list.

from asyncio import set_event_loop


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
        
        # using two pointers, iterate through the list, have slowPointer
        # move one node at a time, have fastPointer move two nodes a time
        # so that fastPointer moves *twice* as fast as slowPointer
        # meaning that when fastPointer hits the end of the list, 
        # slowPointer will point to the middle node

        fastPointer = head
        slowPointer = head
        temp1 = head
        temp2 = head

        while temp2:

            # move the fast pointer ahead by 2 nodes
            
            temp = fastPointer.next  

            if not temp:              # if temp has been assigned to null, we know we've hit the end of the list, return slowPointer.
                return slowPointer    # fastPointer can point to null, but null can't point to anything, meaning that if temp is null
                                      # we have to leave the loop before we get an exception trying to make temp2 = null -> null

            temp2 = temp.next           # can't call .next when the current node is nul
            fastPointer = temp2

            # move the slow pointer ahead by 1 node
            
            slowPointer = slowPointer.next

        return slowPointer

    # testing function

    def test(self, head):
        while head:
            print(head.val)
            head = head.next

# driver code

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


    """
    six = ListNode(6)
    list.append(six)
    five.next = six

    seven = ListNode(7)
    list.append(seven)
    six.next = seven
    """

    s1 = Solution()
    node = s1.reverseList(one)

    print(node.val)

    #while node:
    #    print(node.val)
    #    node = node.next
