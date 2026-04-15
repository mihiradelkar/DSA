class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        i = 1
        if target == words[startIndex]:
            return 0
        while True:
            right = (startIndex + i) % n
            left = (startIndex - i) % n
            if target == words[left] or target == words[right]:
                return i
            i+=1
            if left==right:
                return -1
        