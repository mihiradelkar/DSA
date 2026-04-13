class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        n = len(name)
        for j in range(len(typed)):
            if i<n and name[i] == typed[j]:
                i+=1
            elif j>0 and typed[j] == typed[j-1]:
                pass
            else:
                return False
        return i==n