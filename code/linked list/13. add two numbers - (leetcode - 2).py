"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = 0, 0
        current1, current2 = l1, l2
        place = 1
        while current1 or current2:  # for eleminiating the use of two separate while loops
            if current1 and current2:
                digit1, digit2 = current1.val, current2.val
                num1, num2 = (digit1 * place) + num1, (digit2 * place) + num2
                current1, current2 = current1.next, current2.next
            else:
                if current1 is None:
                    digit2 = current2.val
                    num2 = (digit2 * place) + num2
                    current2 = current2.next
                elif current2 is None:
                    digit1 = current1.val
                    num1 = (digit1 * place) + num1
                    current1 = current1.next

            place *= 10

        total = num1 + num2
        l3 = ListNode(val=0, next=None)
        new_head = l3
        while l3:
            digit = total % 10
            total = int(total / 10)  # or total // 10

            l3.val = digit
            if total == 0:
                break
            l3.next = ListNode(val=None, next=None)
            l3 = l3.next
        return new_head


