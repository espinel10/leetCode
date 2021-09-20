#https://leetcode.com/problems/middle-of-the-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cont=0
        ptr=head
        while ptr!=None:
            cont+=1
            ptr=ptr.next
        cont=cont//2
        while cont!=0:
            cont-=1
            head=head.next
        return head
    
