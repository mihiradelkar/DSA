# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node = {}
        childrens = set()
        
        for parent, child, isLeft in descriptions:
            if parent not in node:
                node[parent] = TreeNode(parent)
            if child not in node:
                node[child] = TreeNode(child)
            childrens.add(child)
            if isLeft:
                node[parent].left = node[child]
            else:
                node[parent].right = node[child]
        
        for parent, _, _ in descriptions:
            if parent not in childrens:
                return node[parent]