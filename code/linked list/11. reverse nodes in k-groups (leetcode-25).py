"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

"""

#----
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # check whther k items exist
        # let initially
        last_of_prev_partition = ListNode(val=0, next=head)
        dummy_head = last_of_prev_partition
        start_of_next_partition = head

        while start_of_next_partition:
            counter = 1
            # current = head
            start_of_current_partition = start_of_next_partition
            current = start_of_current_partition

            is_k_items = False
            while current:  # used to check whether the current partition contains k-items
                if counter == k:
                    is_k_items = True
                    break
                current = current.next
                counter += 1

            if is_k_items:  # if yes, then reverse the current partition
                start_of_next_partition = current.next  # now the current variable has the last node of the current partition, so current.next will be the start of next partition which will be used in next iteration
                last_of_current_partition = current

                # reverse the current k-items
                current = start_of_current_partition  # let us assign current to the start of current_partition. because current was updated in the above while loop which goes to the last node of the partition
                prev = None  # if current partition is 1->2->3 then after reversing 3->2->1->None. this None is from this prev variable
                while current != start_of_next_partition:  # when this condition fails it means that it reached the end of the current partition
                    nxt = current.next  # safe the next value

                    current.next = prev  # reversing

                    prev = current  # updating for next iteration
                    current = nxt

                # after reversing k-items, last_of_current_partition contains the new first node of that partiton after reversing the list(prev variable also contains the same)
                last_of_prev_partition.next = last_of_current_partition  # if 2nd partition is the current partition of this iteration, then the prev partition (i.e 1st partion) would be 3->2->1->none . so now we are making the last node of prev partition (i.e 1) to point the new first node of this current partion(i.e 3->2->1->6->5->4->none)

                while last_of_current_partition.next:  # after reversing, the last of current partiton now becomes the first of current_partition, so to update it to the last value, we are using this loop. now the new last will be none, so condition is checking for none
                    last_of_current_partition = last_of_current_partition.next

                # update : let the current last be the last of prev partition for next iteration
                last_of_prev_partition = last_of_current_partition
            else:  # if there is not enough nodes to satisfy k-items in the partitions, then just add the remaining nodes in the current partition with last node of previous partition
                last_of_prev_partition.next = start_of_current_partition
                break
        return dummy_head.next

