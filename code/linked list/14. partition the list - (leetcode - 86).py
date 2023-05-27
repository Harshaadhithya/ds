"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = ListNode(val=0, next=None)
        right = ListNode(val=0, next=None)
        left_dummy_head = left
        right_dummy_head = right

        current = head
        while current:
            if current.val < x:
                left.next = current
                left = left.next
            else:
                right.next = current
                right = right.next

            current = current.next

        left.next = right_dummy_head.next
        right.next = None  # the right partition may contain other nodes next to it, after the while loop there is no more nodes in the old node, so the current right must be the end of new list, so right.next should be none to make it the end of the list
        return left_dummy_head.next
