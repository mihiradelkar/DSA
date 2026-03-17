class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t_count = { A:1 B:1 C:1 } required_matches = 3
        # s_count = { A:1 D:0 O:0 B:1 E:0 C:1 N:1 }
        # matches = 0 1 2 3 2
        #       0  1  2  3  4  5  6  7  8  9  10 11 12
        # s = " A  D  O  B  E  C  O  D  E  B  A  N  C "
        #                                  L        R
        # res = (inf,0,0) (6,0,5) (4,9,12)
        if not s or not t: return ""                            # empty edge case
        t_count = defaultdict(int)
        for ch in t:                                            # count for t
            t_count[ch]+=1
        required_matches = len(t_count)
        s_count = defaultdict(int)
        left = matches = 0
        res = (float("inf"),0,0)                                # inf if there is no match return ""
        for right, ch in enumerate(s):                          # keep add right
            s_count[ch]+=1
            if ch in t_count and s_count[ch] == t_count[ch]:    # inc match if ch in t and count is same
                matches+=1
            while left<=right and matches==required_matches:    # count matched keep dec left till not matched
                lch = s[left]
                if right-left+1<res[0]:                         # is len less than prev res
                    res = (right-left+1,left,right)             # if yes add len,left,right
                s_count[lch]-=1                                 # dec count
                if lch in t_count and s_count[lch] < t_count[lch]:  # dec if lch in t and count is less
                    matches-=1
                left+=1
        return s[res[1]:res[2]+1] if res[0] != float("inf") else ""
        


        