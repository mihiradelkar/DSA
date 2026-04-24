class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        #                                 s
        # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7  8  9  10
        pos = 0
        free = 0
        for ch in moves:
            if ch == "L":
                pos-=1
            elif ch == "R":
                pos+=1
            else:
                free+=1
        return abs(pos) + free