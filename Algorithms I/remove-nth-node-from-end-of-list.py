#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr=head
        cont=0
        while ptr!=None:
            ptr=ptr.next
            cont+=1
        if cont==1:
            head=head.next
            return head
        if n==cont:
            head=head.next
            return head
        else:
            n=cont-n
        cont=0
        ptr=head
        while cont<n-1:
            ptr=ptr.next
            cont+=1
        ptr.next=ptr.next.next
        return head
