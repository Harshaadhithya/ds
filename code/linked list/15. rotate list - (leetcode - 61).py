"""
Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        dummy = ListNode(next=head)
        if head:
            current = head
            length = 1
            while current.next and current.next.next:  # to find the length, fast iteration
                current = current.next.next
                length += 2
            if current.next:
                length += 1

            k = k % length  # if length = 5, k = 6, then 6 % 5 = 1. for such situation where k>n, if len = 5, k = 5, which means no rotation so 5 % 5 = 0.
            length_of_static_part = length - k  # because if len = 5, k =5, k=k%len = 5%5 = 0, so now k=0. then no rotation and no shifting. so length_of_static_part will be equal to length when there is no rotation.
            if length_of_static_part < length:  # if length of static part = length, then it means no rotation
                current = head
                counter = 1
                while counter < length_of_static_part:
                    current = current.next
                    counter += 1

                start_of_shift_part = current.next
                # if start_of_shift_part:
                current.next = None  # now current contains the end of static part, so it becomes the end of entire node when rotated, so let us assign current.next = None so it becomes the end of entire list.

                dummy.next = start_of_shift_part  # now new head is assigned, which is the start of shift part
                # now we need to link the shift part with the static part

                while start_of_shift_part.next:
                    start_of_shift_part = start_of_shift_part.next
                # now start_of_shift_part contains the end of shift part. now we can link it
                start_of_shift_part.next = head

            return dummy.next


