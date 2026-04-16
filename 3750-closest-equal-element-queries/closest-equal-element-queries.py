class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # n = len(nums)

        # def findDist(i):
        #     dist = 1
        #     # print("i",i)
        #     while dist<=(n//2):
        #         right = (i + dist) % n
        #         left = (i - dist) % n
        #         # print("left", left, nums[left],"right", right, nums[right])
        #         if nums[i] == nums[left] or nums[i] == nums[right]:
        #             return dist
        #         dist+=1
        #     return -1

        # res = []
        # for i in queries:
        #     res.append(findDist(i))
        # return res
        index_map = defaultdict(list)
        for index, num in enumerate(nums):
            index_map[num].append(index)
        # print(index_map)
        n = len(nums)
        res = []
        for i in queries:
            index_list = index_map[nums[i]]
            if len(index_list) <= 1:
                res.append(-1)
                continue
            m = len(index_list)
            pos = bisect_left(index_list,i)
            next_pos = index_list[(pos + 1) % m]
            prev_pos = index_list[(pos - 1) % m]
            dist_next = abs(i-next_pos)
            dist_prev = abs(i-prev_pos)
            circ_next = min(dist_next, n-dist_next)
            circ_prev = min(dist_prev, n-dist_prev)
            res.append(min(circ_next, circ_prev))
        return res
        