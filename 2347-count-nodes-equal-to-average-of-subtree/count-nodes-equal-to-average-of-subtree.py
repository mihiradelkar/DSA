# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node):
            if not node:
                return (0,0)
            l_sum,l_cnt = dfs(node.left)
            r_sum,r_cnt = dfs(node.right)
            # sum of left + right + cur
            t_sum = l_sum+r_sum+node.val
            # count of left + right + 1
            t_cnt = l_cnt+r_cnt+1
            if node.val == t_sum//t_cnt:
                self.count+=1
            return (t_sum,t_cnt)
        dfs(root)
        return self.count
        