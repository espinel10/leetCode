# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left==right: return head
        dummy= ListNode(0,next=head)
        prev= dummy
        i=1
        while i < left:
            prev = prev.next
            i+=1
        cur = prev.next
        nx = cur.next
        while i < right:
            tmp = nx.next
            nx.next = cur
            cur =nx
            nx = tmp
            i+=1
        prev.next.next = nx
        prev.next =cur
        
        return dummy.next
