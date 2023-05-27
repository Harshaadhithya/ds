# You are given the head of a singly linked - list.The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
#
# Example
# 1:
#
# Input: head = [1, 2, 3, 4]
# Output: [1, 4, 2, 3]


# --------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # to find the middle node
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # slow has the middle value of the list
        middle = slow
        # now reverse the second half of the list, (i.e after the middle element)
        prev = None
        current = middle.next
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        # now prev contains the tail node, which will be the new head of the second half
        # 1->2->3->4->5->6->7
        # here middle = 4
        # first half = 1->2->3->4  ,here the last node 4 still points to 5, which is now in the second half
        # second half = 5->6->7
        # second half after reversing = 7->6->5->None
        # to print = 1->7->2->6->3->5->4
        # the condition for ending the loop or travesal is that when first half reaches the end(i.e after the middle element). to find that we must make the last element of the first half (i.e middle of entire list) to point to None
        # so first let us make the middle to point to None
        middle.next = None
        left = head
        right = prev
        while right:
            left_safe = left.next
            right_safe = right.next

            left.next = right
            right.next = left_safe

            left = left_safe
            right = right_safe