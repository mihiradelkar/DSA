class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # n = len(s)
        # if len(goal)!=n:
        #     return False
        # i = 0
        # j = 0
        # while s[i] != goal[j]:
        #     i+=1
        # while j < n:
        #     if s[(i+j)%n] != goal[j]:
        #         return False
        #     j+=1
        # return True

        if len(s) != len(goal):
            return False
        return goal in s+s
        