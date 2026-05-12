class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0]-x[1])
        curr = 0
        used = 0
        for a, r in tasks:
            add = max(0, r - curr)   # ← fix here
            curr += add
            used += add
            curr -= a
        return used



        # s_task = [(a,r,r-a) for a,r in tasks]
        # s_task = sorted(s_task, key=lambda x: (x[2],x[1]))
        # # print(s_task)
        # curr = 0
        # req = 0
        # for a,r,_ in s_task:
        #     req+=a
        #     curr+=a
        #     if curr<r:


        # print(curr)
        # return req
        
        