# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def recursiveReverse(current, prev):
    if current is None:
        return prev
    nxt = current.next
    current.next = prev
    # prev = current
    # current = nxt
    return recursiveReverse(current=nxt, prev=current)


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        # using recursion
        return recursiveReverse(current, prev)
        #-----
        # using iteration
        while current:
            nxt = current.next

            current.next = prev

            prev = current
            current = nxt

        # when while loop ends, then current must have None and prev must have the last node.
        # new_head = prev
        return prev