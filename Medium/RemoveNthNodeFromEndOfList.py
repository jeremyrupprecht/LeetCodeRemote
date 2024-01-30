# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next == None and n == 1:
            return None

        current = head
        remove = head
        prev = head
        while current.next:
            current = current.next
            n -= 1
            if (n < 1):
                prev = remove
                remove = remove.next
                
        if prev == head and remove == head:
            temp = head
            head = head.next
            temp = None
            return head

        # Current is at its final node
        if current == remove:
            prev.next = None
        else:
            prev.next = prev.next.next

        return head

if __name__ == "__main__":

    # Create the nodelist
    nodes = ListNode(1)
    nodesHead = nodes
    numberOfNodes = 6
    for i in range(2, numberOfNodes):
        node = ListNode(i)
        nodes.next = node
        nodes = nodes.next

    s1 = Solution()
    s1.removeNthFromEnd(nodesHead, 2)

    while (True):
        print(nodesHead.val)

        if nodesHead.next == None:
            break
        
        nodesHead = nodesHead.next