class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # MOD = 10**9 + 7
        # for l, r, k, v in queries:
        #     idx = l
        #     while idx <= r:
        #         nums[idx] = (nums[idx] * v) % MOD
        #         idx += k
        # print(nums)
        # res = 0
        # for x in nums:
        #     res^=x
        # return res
        
        # REDO for Streaks 
        MOD = 10**9 + 7
        n = len(nums)
        B = max(1, int(n**0.5))
    
        # only allocate lazily for (k, res) pairs that get touched
        lazy = {}
        touched = set()  # track which (k, res) pairs are active
    
        for l, r, k, v in queries:
            if k > B:
                # large k: < sqrt(n) elements touched, apply directly
                idx = l
                while idx <= r:
                    nums[idx] = nums[idx] * v % MOD
                    idx += k
            else:
                res = l % k
                a = l // k
                b = a + (r - l) // k
                key = (k, res)
                if key not in lazy:
                    lazy[key] = [1] * (n // k + 2)
                lazy[key][a] = lazy[key][a] * v % MOD
                lazy[key][b + 1] = lazy[key][b + 1] * pow(v, MOD - 2, MOD) % MOD
                touched.add(key)
    
        # only apply pairs that were actually touched
        for (k, res) in touched:
            arr = lazy[(k, res)]
            prefix = 1
            j = 0
            for idx in range(res, n, k):
                prefix = prefix * arr[j] % MOD
                if prefix != 1:  # skip no-op multiplications
                    nums[idx] = nums[idx] * prefix % MOD
                j += 1
    
        result = 0
        for x in nums:
            result ^= x
        return result