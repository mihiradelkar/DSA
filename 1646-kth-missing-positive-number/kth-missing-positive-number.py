class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # [2,3,4,7,11], k = 5
        #  l   m    r  4-(2+1) = 1>=5 no 
        #        lm r  7-(3+1) = 3>=5 no
        #          lr  4+5 = 9
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] - (mid + 1) >= k:
                hi = mid
            else:
                lo = mid + 1
    
        # answer = lo + k
        # (lo elements in arr before it, k missing offsets)
        return lo + k    
    