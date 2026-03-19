class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_freq = 0
        res = 0
        freq = defaultdict(int)
        while right<len(s):
            freq[s[right]]+=1
            max_freq = max(max_freq,freq[s[right]])
            while (right-left+1)-max_freq > k:
                freq[s[left]]-=1
                left+=1
            res = max(res,right-left+1)
            right+=1
        return res
        