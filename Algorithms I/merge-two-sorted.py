#https://leetcode.com/problems/merge-two-sorted-lists/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        refer=None
        if l1==None and l2==None:
            refer=l1
            return refer 
        if l1==None:
            return l2
        if l2==None:
            return l1
        
        def recursion(l1,l2,ref):
            if l1==None and l2==None:
                return
            if l2==None or l1==None:
                if l2==None:
                    ref.next=ListNode(l1.val)
                    recursion(l1.next,l2,ref.next)
                else:
                    ref.next=ListNode(l2.val)
                    recursion(l1,l2.next,ref.next)
            else:
                if l1.val < l2.val:
                    ref.next=ListNode(l1.val)
                    recursion(l1.next,l2,ref.next)
                else:
                    ref.next=ListNode(l2.val)
                    recursion(l1,l2.next,ref.next)
        if l1.val < l2.val:
            refer=ListNode(l1.val)
            recursion(l1.next,l2,refer)
        else:
            refer=ListNode(l2.val)
            recursion(l1,l2.next,refer)
            
        return refer
                
