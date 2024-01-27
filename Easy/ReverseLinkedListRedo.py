# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        restOfList = None
        while current != None:
            restOfList = current.next
            current.next = prev

            prev = current
            current = restOfList

        return prev

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
    
