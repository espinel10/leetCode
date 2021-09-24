#https://leetcode.com/problems/merge-two-binary-trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1==None and root2==None:
            return None
        root=TreeNode()
        def recorrer(leaf1,leaf2,rot):
            val=0
            if leaf1!=None:
                val+=leaf1.val
            if leaf2!=None:
                val+=leaf2.val
            rot.val=val
            ptr1,ptr2=None,None
            if leaf1!=None:
                ptr1=leaf1.left
            if leaf2!=None:
                ptr2=leaf2.left
            if ptr1!=None or ptr2!=None:
                rot.left=TreeNode()
                recorrer(ptr1,ptr2,rot.left)       
            ptr1,ptr2=None,None
            if leaf1!=None:
                ptr1=leaf1.right
            if leaf2!=None:
                ptr2=leaf2.right
            if ptr1!=None or ptr2!=None:
                rot.right=TreeNode()
                recorrer(ptr1,ptr2,rot.right)
        recorrer(root1,root2,root)
        return root
