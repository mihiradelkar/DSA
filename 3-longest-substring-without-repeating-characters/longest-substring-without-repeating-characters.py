class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_l = 0
        mapp = {}
        for end, ch in enumerate(s):
            if ch in mapp and mapp[ch]>=start: # if char in map and char[idx] is after start point
                start = mapp[ch]+1
            mapp[ch] = end
            max_l = max(max_l,end-start+1)
        return max_l
