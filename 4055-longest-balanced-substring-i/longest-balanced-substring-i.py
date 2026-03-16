class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for left in range(n):
            freq = defaultdict(int)
            for right in range(left,n):
                freq[s[right]]+=1
                if len(set(freq.values())) == 1:
                    res = max(res, right-left+1)
        return res