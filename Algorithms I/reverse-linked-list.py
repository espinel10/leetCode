#https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        edges=[]
        ref=head
        while ref!=None: 
            edges.append(ref)
            ref=ref.next 
            
        edges[0].next=None
        for i in range(len(edges)-1,0,-1):
            edges[i].next=edges[i-1]
        head=edges[-1]
        return head
