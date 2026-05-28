class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # n = len(nums)
        # res = 0
        # for i in range(n):
        #     max_n = nums[i]
        #     min_n = nums[i]
        #     for j in range(i,n):
        #         max_n = max(max_n,nums[j]) 
        #         min_n = min(min_n,nums[j]) 
        #         if max_n - min_n <= limit:
        #             res = max(res,j-i+1)
        #         else:
        #             break
        # return res
                    
        # n = len(nums)
        # res = 0
        # inc_q = deque()
        # dec_q = deque()
        # l = 0
        # for r, num in enumerate(nums):
        #     while inc_q and nums[inc_q[-1]]>=num:
        #         inc_q.pop()
        #     inc_q.append(r)

        #     while dec_q and nums[dec_q[-1]]<=num:
        #         dec_q.pop()
        #     dec_q.append(r)

        #     while nums[dec_q[0]]-nums[inc_q[0]] > limit:
        #         if inc_q[0] == l: inc_q.popleft()
        #         if dec_q[0] == l: dec_q.popleft()
        #         l+=1
            
        #     # print("inc_q",inc_q)
        #     # print("dec_q",dec_q)
        #     # print("")
        #     res = max(res,r-l+1)
        # return res

        l = 0
        max_q = deque()
        min_q = deque()
        res = 0
        for r, num in enumerate(nums):
            while max_q and max_q[-1]<num:
                max_q.pop()
            max_q.append(num)

            while min_q and min_q[-1]>num:
                min_q.pop()
            min_q.append(num)

            while max_q[0]-min_q[0] > limit:
                if max_q[0] == nums[l]:
                    max_q.popleft()
                if min_q[0] == nums[l]:
                    min_q.popleft()
                l+=1

            res = max(res,r-l+1)

        return res 
        