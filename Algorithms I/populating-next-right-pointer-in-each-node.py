##https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root==None:
            return root
        nodes=[[root]]
        while True:
            aux=[]
            for ptr in nodes[-1]:
                if ptr==None:
                    continue
                aux.append(ptr.left)
                aux.append(ptr.right)
            if len(aux)==0:
                break
            for i in range(len(aux)-1):
                if aux[i]==None:
                    continue
                aux[i].next=aux[i+1]
            nodes.append(aux)
        return root
        
