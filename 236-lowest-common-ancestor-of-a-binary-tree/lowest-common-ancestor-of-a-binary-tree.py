# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Question:
        # does p and q exists 
        # if root null ?
        # p !=  q ?
        # tree have unique values ?
        # return val or tree node?

        # Approach:
        # dfs: 
        # find p or q and found return node up
        # if not dfs left and right
        # if both not null then root is lca
        # if left found keep bubbling up left
        # if right found keep bubbling up right

        if not root:
            return None
        if root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left or right
        # if left:
        #     return left
        # else:
        #     return right
        
        # p = 5, q = 1  4
        #        3
        #    5       1
        #  6   2   0   8 
        # n n 7 4