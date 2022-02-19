# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        ptr=head
        node=ListNode(0)
        result=node
        ref=-9999999
        while ptr.next!=None:
            if ref!=ptr.val:
                if ptr.val!=ptr.next.val:
                    node.next=ListNode(ptr.val)
                    node=node.next
                else:
                    ref=ptr.val
            ptr=ptr.next
        if ptr.val!=ref:
            node.next=ListNode(ptr.val)
        return result.next
