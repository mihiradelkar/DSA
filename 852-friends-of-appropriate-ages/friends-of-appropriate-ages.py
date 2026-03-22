class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # n = len(ages)
        # res = 0
        # for x in range(n):
        #     for y in range(n):
        #         if x==y:
        #             continue
        #         if ages[y] > 0.5 * ages[x] + 7 and  ages[y] <= ages[x]:
        #             res+=1
        # return res
        
        # Optimal Approach
        n = len(ages)
        res = 0
        count = Counter(ages)

        for age_x, count_x in count.items():
            for age_y, count_y in count.items():
                if age_y > 0.5 * age_x + 7 and age_y <= age_x:
                    if age_x==age_y:
                        res += count_x * (count_x-1)
                    else:
                        res += count_x * count_y
        return res