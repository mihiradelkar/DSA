class Solution:
    def minimumDeletions(self, s: str) -> int:
        # min_d = float("inf")
        # for i in range(len(s)):
        #     cost = s[:i].count("b") + s[i:].count("a")
        #     min_d = min(min_d,cost)
        # return min_d

        count_b = 0
        deletions = 0
        for ch in s:
            if ch == "b":
                count_b+=1
            elif count_b>0:
                    count_b-=1
                    deletions+=1
        return deletions