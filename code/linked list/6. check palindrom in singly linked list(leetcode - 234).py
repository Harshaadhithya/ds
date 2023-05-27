class Solution(object):
    def isPalindrome(self, head):

        """
        :type head: ListNode
        :rtype: bool
        """
        # to find the middle node. if 1--2--3--4--5--6 ,3 is the middle node. if 1--2--3--4--5--6--7, then 4 is the middle node. in case 2, [1,2,3] and [5,6,7] is compared. in case 1, [1,2,3] and [4,5,6] is compared.
        fast_pointer = head
        slow_pointer = head
        while fast_pointer.next and fast_pointer.next.next:  # when n = 7(odd) index=[0-6], if fast pointer is at 6(it can't go beyond 6, which is the last index), then slow pointer will be in 3. so 3 is the middle node. the second part of the linked list will start from middle+1 (i.e.)4 which means the second portion is 4,5,6.
            # if n=8(even) index[0-7], if fast pointer is at 6(it cant go beyond 7, but the possible value for fast pointer is any even number because it jumps two node at a time,so it is at 6) , then slow pointer will be at 3, then 3 is the middle node, then the second part will be the remaining part after the middle node which is 4,5,6,7.
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        middle_node = slow_pointer

        # reverse the second half, i.e after the middle node.
        prev = None
        current = middle_node.next
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        # when the loop ends, current will hold None and the prev will hold the last node.

        left = head
        right = prev
        while right is not None:  # the starting node of the second part i.e after the middle node, it points to none.
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

