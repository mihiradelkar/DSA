class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        s_task = [(a,r,r-a) for a,r in tasks]
        s_task = sorted(s_task, key=lambda x: (-x[2],-x[1]))
        # print(s_task)
        curr = 0
        used = 0
        for a,r,_ in s_task:
            # print(a,r)
            add = max(0, r - curr)
            curr+=add
            used+=add
            curr-=a
        # print(curr)
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
        
        