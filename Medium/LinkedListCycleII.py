# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        Dict = {}
        
        current = head
        
        while current:
            
            if not current in Dict:
                Dict[current] = current.val
                current = current.next
            else:
                return current

        return None

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

    # this node cycles back to node 4

    six = ListNode(6)
    list.append(six)
    five.next = six
    six.next = four


    s1 = Solution()
    node = s1.detectCycle(one)
    print(node.val)

#    while node:
#        print(node.val)
#        node = node.next
