class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # total = defaultdict(list)
        # for i in range(n//2):
        #     total[nums[i] + nums[n - 1 - i]].append(i)
        #     # if total[i]:
        # return len(total)-1

        # Optimal
        n = len(nums)
        diff = [0] * (2*limit+2)
        #   T [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #      0  1  2  3  4  5  6  7  8  9
        # invalid^  min(1+1)       max(2*limit)
        for i in range(n//2):
            lo = min(nums[i], nums[n - 1 - i])
            hi = max(nums[i], nums[n - 1 - i])
            # Base: T == 2 both should be 1,1
            diff[2] += 2
            
            diff[lo+1]-=1           # low 
            diff[hi+limit+1]+=1

            diff[lo+hi]-=1
            diff[lo+hi+1]+=1
            # print(diff)
        # Cost to bring all the number at the target.
        # index: [0, 0, 1, 0, -1, 1,  0,  0,  1,  0] (lo=1,hi=3)
        #     T:        2  3   4  5   6   7   8
        # index: [0, 0, 3, -1, -1, 1, -1,  1,  1,  1] (lo=2,hi=4)
        #     T:        2   3   4  5   6   7   8
        # initial high to bring all the lowest, and keeps reducing and again inreasing as we go higher target
        res,curr = n,0
        for t in range(2,2*limit+1):
            curr+=diff[t]
            res = min(curr,res)
        return res
        # T=2:  0+3   = 3
        # T=3:  3-1   = 2
        # T=4:  2-1   = 1   <- minimum
        # T=5:  1+1   = 2
        # T=6:  2-1   = 1   <- also minimum
        # T=7:  1+1   = 2
        # T=8:  2+1   = 3