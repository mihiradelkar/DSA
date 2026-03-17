# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Question:
        # if left nodes has more height it will be visible right?
        # will the root be null? return []
        # 
        # Approach:
        # dfs: keep going right and add nodes to list check left if height is more then recorded add to list
        
        # def dfs(node,level):
        #     if not node: return None
        #     if level==len(res): res.append(node.val)
        #     dfs(node.right,level+1) dfs(node.left,level+1)

        # bfs: for each level add the last element

        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            last = None 
            for _ in range(len(queue)):
                node = queue.popleft()
                last = node.val
                # if i==level_nodes-1:
                #     res.append(curr.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(last)
        return res
        
        #        1
        #    2       3
        #  n   5   n   4
        # n n n 7
        # [1,3,4,7]