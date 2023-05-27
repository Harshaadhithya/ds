"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node.
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

"""

# -------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev_of_slow = None
        slow = head
        fast = head
        while fast:
            if fast.next is None:   #if the n is odd, then fast at last reaches the tail node, so we are checking fast is the last node or not using this condition.
                break
            elif fast.next.next is None:  #if n is even, then fast at last reaches the last before node, so we are checking fast is at the last before node or not using this condition.
            # if n = 4, n/2 =2, the middle element is 3, which means (n/2)+1 is the middle element so solw is updated to next element and returned
                prev_of_slow = slow
                slow = slow.next
                break
            prev_of_slow = slow
            slow = slow.next
            fast = fast.next.next

        # here slow is the middle element which is to be deleted from the list
        # print(slow.val,prev_of_slow)
        if prev_of_slow is None:   #it implies that there is only one node in linked list, so it must be the middle, so it must be deleted, so delete the head node
            head = None
        else:
            prev_of_slow.next = slow.next

        return head