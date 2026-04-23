class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # im = defaultdict(list)
        # for i, num in enumerate(nums):
        #     im[num].append(i)
        # print(im)
        # res = []
        # for i, num in enumerate(nums):
        #     total = 0
        #     for j in im[num]:
        #         total += abs(i-j)
        #     res.append(total)
        # return res

        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)
        n = len(nums)
        res = [0] * n
        for indices in index_map.values():
            m = len(indices)
            prefix = 0
            # print(indices)
            for i, idx in enumerate(indices):
                res[idx] += i * idx - prefix
                # print(res[idx], i, idx, prefix)
                prefix += idx
            
            suffix = 0
            # print(res)
            for i in range(m-1,-1,-1):
                idx = indices[i]
                right_count = m-1-i
                res[idx] += suffix - right_count * idx
                # print(res[idx], suffix, right_count, idx)
                suffix += idx
            # print(res)
        return res


