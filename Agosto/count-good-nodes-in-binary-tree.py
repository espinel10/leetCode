#https://leetcode.com/problems/count-good-nodes-in-binary-tree/solution/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cont=0
    def recursion(self,leaf,k):
        if leaf==None:
            return
        else:
            if leaf.val>=k:
                self.cont+=1    
        self.recursion(leaf.left,max(k,leaf.val))
        self.recursion(leaf.right,max(k,leaf.val))

    def goodNodes(self, root: TreeNode) -> int:
        self.recursion(root,root.val)
        return self.cont
