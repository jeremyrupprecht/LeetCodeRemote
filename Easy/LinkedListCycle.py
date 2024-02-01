# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):

    def hasCycleDict(self, head):
        Dict = {}
        current = head
        while current:
            if (current.val, current.next) in Dict:
                return True
            else:
                Dict[(current.val, current.next)] = current

            current = current.next

        return False

    def hasCycleOnePointer(self, head):
        current = head
        while current:
            if current.val == "Visited":
                return True

            current.val = "Visited"
            current = current.next	

        return False


    def hasCycleTwoPointers(self, head):
        if head == None or head.next == None:
            return False

        fast = head
        slow = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":

    node0 = ListNode(3)
    node1 = ListNode(2)
    node0.next = node1
    node2 = ListNode(0)
    node1.next = node2
    node3 = ListNode(4)
    node2.next = node3
    # node3.next = node2

    s1 = Solution()
    print(s1.hasCycleDict(node0))
    print(s1.hasCycleOnePointer(node0))
    print(s1.hasCycleTwoPointers(node0))