class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        @cache
        def dp(i):
            best = 1
            # left
            for j in range(i-1,max(-1,i-d-1),-1):
                if arr[i] <= arr[j]:
                    break
                best = max(best,1+dp(j))

            for j in range(i+1,min(n,i+d+1)):
                if arr[i] <= arr[j]:
                    break
                best = max(best,1+dp(j))
            return best
        return max(dp(i) for i in range(n))