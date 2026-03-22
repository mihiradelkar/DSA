class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start,curr):
            res.append(curr[:])
            for i in range(start,len(nums)):
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()
        backtrack(0,[])
        return res

























        res = []
        cur = []
        # [1,2,3]
        # [1]
        # [[],[1],[1,2],[1,2,3],]
        # [2]
        # b(2)
        def backtrack(start):
            res.append(cur[:])
            # print(res)
            for i in range(start,len(nums)):
                cur.append(nums[i])
                # print("backtrack "+str(i+1))
                backtrack(i+1)
                # print(i,cur[-1])
                cur.pop()
        backtrack(0)
        return res
        