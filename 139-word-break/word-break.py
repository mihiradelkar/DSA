class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1,n+1):
            # for j in range(i):
            for j in wordDict:
                # print(s[j:i],j,i)
                # if dp[j] and s[j:i] in word_set:
                if i>=len(j) and dp[i-len(j)] and s[i-len(j):i]==j:
                    dp[i] = True
                    break
        # print(dp)
        return dp[n]