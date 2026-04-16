class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # [0, 1, 2, 3, 4] n=5 s=0 t=9
        #  S  R        L
        #  S     R  L
        #  S     L  R
        #  S  L        R
        # SLR
        n = len(words)
        i = 1
        if target == words[startIndex]:
            return 0
        while i<=(n//2):
            if target == words[(startIndex - i) % n] or target == words[(startIndex + i) % n]:
                return i
            i+=1
        return -1
        