"""

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)



Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
"""

# ----
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is not None:  #if i/p is [] then o/p is none
            current_node = head
            next_node = current_node.next
            i = 0 #this counter is used to get the new head after swapping
            new_head = head #for now let it be hed, because if there is only one node in the list then it will not go inside loop for swapping, so return the head as the new head
            while next_node:  #if we have pairs of node, then we can swap, if the next node of the current node is none, then it means that no pair to swap, only one node is left.
                next_next_node = next_node.next #safing the next next node for next iteraton, it becomes the current node for next iteration.
                next_node.next = current_node

                if i==0:
                    new_head = next_node

                if next_next_node is None:
                    current_node.next = None #this is used to break the cycle, if not done then the last node would point to someother node without getting terminated hwich then forms a cycle.
                    break
                else:
                    if next_next_node.next is None:
                        #if at last. only one node is left , then no swapping is done for next iteration, so just link this node to the previously swapped node
                        current_node.next = next_next_node
                    else:
                        current_node.next = next_next_node.next

                    current_node = next_next_node
                    next_node = next_next_node.next
                    i+=1
            return new_head


"""
neetcode method
"""


# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         prev = ListNode(val=None,next=head)
#         current = head
#         dummy = prev
#         while current and current.next:
#             second = current.next
#             #safe
#             nxt_pair = second.next
#
#             #swap
#             second.next = current
#             current.next = nxt_pair
#             prev.next = second
#
#             #update
#             prev = current
#             current = nxt_pair #or current.next
#
#         return dummy.next
