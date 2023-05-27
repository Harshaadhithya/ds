#this is a correct solution,but time complexity is high. i haven't used merge sort for this.

"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # lists = [1_head,2_head,3_head]
        # new_head = ListNode(val = None, next = None)
        dummy = ListNode(val=None, next=None)

        # no_of_available_lists = len(lists)
        is_lists_has_elements = bool(len(lists))
        while is_lists_has_elements:  # this while is used to iterate until all the nodes of all the linked lists are visited
            i = 0
            is_lists_has_elements = False
            while i < len(
                    lists):  # this while is used to iterate all the linked list to get the current head of all the linked lists in the array. if there are 3 linked lists. then if i=0, then it denotes 1st linked-list, i gets updated to 3-1 =2, and after that the loop gets ended.

                new_list_pointer = dummy
                if lists[i] is None:
                    pass
                else:
                    is_lists_has_elements = True
                    new_node = ListNode(val=lists[i].val)
                    # here omne doubt onlinegdb

                    # while new_list_pointer.next.val is not None or lists[i].val > new_list_pointer.next.val:
                    while new_list_pointer.next is not None:
                        if lists[i].val <= new_list_pointer.next.val:
                            # new_node = ListNode(val = lists[i].val)
                            new_node.next = new_list_pointer.next
                            new_list_pointer.next = new_node
                            break

                        new_list_pointer = new_list_pointer.next

                    if new_list_pointer.next is None:
                        new_list_pointer.next = new_node
                        # new_list_pointer.next.val = lists[i].val

                    lists[i] = lists[i].next
                i += 1
        return dummy.next





