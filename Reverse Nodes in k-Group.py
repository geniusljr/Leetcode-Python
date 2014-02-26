# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):

        def reverse(pre, later):
            last = pre.next
            cur = last.next
            while cur != later:
                last.next = cur.next
                cur.next = pre.next
                pre.next = cur
                cur = last.next
            return last

        if head == None or k == 1:
            return head
        preHead = ListNode(-1)
        preHead.next = head
        pre = preHead
        count = 0
        while head != None:
            count = count + 1
            if count % k == 0:
                pre = reverse(pre, head.next)
                head = pre.next
            else:
                head = head.next
        return preHead.next
        
