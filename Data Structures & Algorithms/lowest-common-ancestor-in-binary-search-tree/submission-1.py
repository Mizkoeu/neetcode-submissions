# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lo, hi = min(p.val, q.val), max(p.val, q.val)
        if lo <= root.val and hi >= root.val:
            return root
        if lo > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif hi < root.val:
            return self.lowestCommonAncestor(root.left, p, q)