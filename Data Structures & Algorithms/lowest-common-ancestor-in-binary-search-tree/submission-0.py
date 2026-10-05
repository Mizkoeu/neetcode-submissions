# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        left_lst = []
        right_lst = []
        left_lst = self.findBFSPath(root, p, left_lst)
        right_lst = self.findBFSPath(root, q, right_lst)
        
        lca = root
        for u, v in zip(left_lst, right_lst):
            if u == v:
                lca = u
            else:
                break
        return lca

    def findBFSPath(self, root, t, lst):
        lst.append(root)

        if t.val == root.val:
            return lst
        
        if t.val > root.val:
            root = root.right
            return self.findBFSPath(root, t, lst)
        else:
            root = root.left
            return self.findBFSPath(root, t, lst)