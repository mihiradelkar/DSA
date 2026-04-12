class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
         
        #    [[2,5,3],
        #     [2,6,5],
        #     [1,2,5],
        #     [5,2,3]], 
        # T = [5,5,5]

        # [[3,4,5],
        #  [4,5,6]], 
        #T=[3,2,5]
        # memo = [False]*3
        # for i in range(3):
        #     for j in range(len(triplets)):
        #         if target[i]==triplets[j][i]:
        #             memo[i] = True
        #             break

        # for m in memo:
        #     if not m:
        #         return False
        # return True
        
        
        #  [2,7,5]
        #  [0,0,0]
        # [[2,5,3],
        #  [1,8,4],
        #  [1,7,5]], 
        
        merged = [0,0,0]
        x,y,z = target
        for a,b,c in triplets:
            if a<=x and b<=y and c<=z:
                merged = [max(a, merged[0]), max(b, merged[1]), max(c, merged[2])]
        return merged == target
