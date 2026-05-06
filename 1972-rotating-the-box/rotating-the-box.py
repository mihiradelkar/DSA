class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # m = len(boxGrid)
        # n = len(boxGrid[0])

        # new_box = [["-"]*m for _ in range(n)]

        # for i in range(m):
        #     for j in range(m):
        #         new_box[j][i] = boxGrid[i][j]
        # return new_box
        m, n = len(box), len(box[0])

        # Phase 1 — gravity: stones fall right, blocked by obstacles
        for i in range(m):
            empty = n - 1                      # next available landing slot
            for j in range(n - 1, -1, -1):
                if box[i][j] == '#':
                    box[i][j] = '.'            # clear source
                    box[i][empty] = '#'        # place at landing spot
                    empty -= 1                 # next slot is one further left
                elif box[i][j] == '*':
                    empty = j - 1              # reset: obstacle blocks rightward fall

        # Phase 2 — rotate 90° CW: (i, j) → (j, m-1-i) in result of size n×m
        res = [[''] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = box[i][j]

        return res
