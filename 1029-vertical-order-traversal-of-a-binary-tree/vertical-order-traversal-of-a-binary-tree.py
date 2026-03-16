# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_map = defaultdict(list)
        queue = deque([(root,0,0)])
        min_col = 0
        max_col = 0
        while queue:
            node,row,col = queue.popleft()
            col_map[col].append((row,node.val))
            min_col = min(min_col,col)
            max_col = max(max_col,col)
            if node.left:
                queue.append((node.left,row+1,col-1))
            if node.right:
                queue.append((node.right,row+1,col+1))
        res = []
        for col in range(min_col,max_col+1):
            sorted_nodes = sorted(col_map[col])
            res.append([val for _,val in sorted_nodes])
        return res