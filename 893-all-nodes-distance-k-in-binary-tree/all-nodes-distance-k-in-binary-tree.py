# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        def dfs(node,par):
            if not node:
                return
            parent[node] = par
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root,None)
        # print(parent)

        queue = deque([target])
        visited = {target}
        dist = 0

        while queue:
            if dist == k:
                return [node.val for node in queue]
            
            dist += 1

            for _ in range(len(queue)):
                node = queue.popleft()  # important pop left
                for neighbor in [node.left,node.right,parent[node]]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return []
