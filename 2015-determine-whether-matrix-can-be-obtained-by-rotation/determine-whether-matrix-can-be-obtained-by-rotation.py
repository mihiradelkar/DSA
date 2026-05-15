class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def rotate90(m):
            return [[m[n-1-j][i] for j in range(n)] for i in range(n)]
        curr = mat
        for _ in range(4):
            if curr == target:
                return True
            curr = rotate90(curr)
        return False

        