# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        seen = {}
        childs = set()
        for parent, child, isLeft in descriptions:
            if parent not in seen:
                seen[parent] = TreeNode(parent)
            if child not in seen:
                seen[child] = TreeNode(child)
            childs.add(child)
            if isLeft:
                seen[parent].left = seen[child]
            else:
                seen[parent].right = seen[child]
        for k in seen.keys():
            if k not in childs:
                return seen[k]