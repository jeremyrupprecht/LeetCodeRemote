# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/description/

# lol can't run this one, the set up for this one is painful just run it on the leetcode site

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        current = head
        Dict = {}
        while current:
            node = Node(current.val, None, None)
            Dict[current] = node
            current = current.next
            
        current2 = head
        copyHead = None
        copyCurrent = None
        if head in Dict:
            copyHead = Dict[head]
            copyCurrent = copyHead
            
        while current2:		
            copyNext = None
            copyRandom = None

            if current2 in Dict:
                copyCurrent = Dict[current2]
            if current2.next in Dict:
                copyNext = Dict[current2.next]
            if current2.random in Dict:
                copyRandom = Dict[current2.random]

            copyCurrent.next = copyNext
            copyCurrent.random = copyRandom

            current2 = current2.next
            copyCurrent = copyCurrent.next
            
        return copyHead
