class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # queue = [0]
        # visited = {0}
        # while queue:
        #     curr = queue.pop()
        #     if curr == n-1:
        #         return True
        #     for nxt in range(curr+maxJump,curr+minJump-1,-1):
        #         if nxt<n and s[nxt] == "0":
        #             queue.append(nxt)
        #             visited.add(nxt)
        # return False

        # @cache
        # def dfs(curr):
        #     if curr == n-1:
        #         return True

        #     for nxt in range(curr+maxJump,curr+minJump-1,-1):
        #         if nxt<n and s[nxt] == "0":
        #             if dfs(nxt):
        #                 return True
        #     return False

        # return dfs(0)

        n = len(s)

        if s[-1] == '1':
            return False
    
        dp     = [False] * n
        dp[0]  = True
        prefix = [0] * (n + 1)   
        prefix[1] = 1            
    
        for i in range(1, n):
            if s[i] == '0':   
                lo = max(0, i - maxJump)  
                hi = i - minJump
                if hi >= 0:   
                    count = prefix[hi + 1] - prefix[lo]
                    if count > 0:
                        dp[i] = True
    
            prefix[i + 1] = prefix[i] + (1 if dp[i] else 0)
        return dp[-1]