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
        head = None
        
        temp = None
        
        carry = 0
        #loop for the tow lists
        while l1 is not None or l2 is not None:
            sum_value = carry
            if l1 is not None:
                sum_value += l1.val
                l1 = l1.next

            if l2 is not None:
                sum_value += l2.val
                l2 = l2.next


            node = ListNode(sum_value % 10)

            carry = sum_value // 10
            if temp is None:
                temp = head = node
            else:
                temp.next = node
                temp = temp.next
        #after the last iteration, we will check if there is carry left
        if carry > 0:
            temp.next = ListNode(carry)
        return head
            