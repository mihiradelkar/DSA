class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        for l, r, k, v in queries:
            # idx = l
            # while idx <= r:
            #     nums[idx] = (nums[idx] * v) % MOD
            #     idx += k
            for idx in range(l, r + 1, k):
                nums[idx] = (nums[idx] * v) % MOD

        res = 0
        for x in nums:
            res ^= x
        return res
        