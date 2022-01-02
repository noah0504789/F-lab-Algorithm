class Solution:
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(-1)
        dummy.next = head

        back = dummy
        front = dummy

        for i in range(n):
            front = front.next

        while front.next != None:
            front = front.next
            back = back.next

        back.next = back.next.next

        return dummy.next