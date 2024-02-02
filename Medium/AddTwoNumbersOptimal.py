# from leetcode video
# https://leetcode.com/problems/add-two-numbers/

def addTwoNumbers(self, l1, l2):
    dummy = ListNode()
    current = dummy

    carry = 0
    while l1 or l2 or carry:
        if l1:
            v1 = l1.val
        else:
            v1 = 0

        if l2:
            v2 = l2.val
        else:
            v2 = 0
        # compute new digit
        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10 # grab LSD
        current.next = ListNode(val)
        
        # update pointers
        current = current.next
        if l1:
            l1 = l1.next
        else:
            l1 = None
        if l2:
            l2 = l2.next
        else:
            l2 = None

    return dummy.next

