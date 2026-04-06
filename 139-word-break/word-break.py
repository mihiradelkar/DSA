class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)+1
        word_set = set(wordDict)
        dp = [False] * (n)
        dp[0] = True
        for i in range(1,n):
            for j in range(i):
                # print(s[j:i],j,i)
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        # print(dp)
        return dp[n-1]