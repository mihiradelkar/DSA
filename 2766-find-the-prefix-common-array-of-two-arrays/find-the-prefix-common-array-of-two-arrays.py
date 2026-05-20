class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # A = [1,3,2,4], 
        # B = [3,1,2,4]
        # C = [0,2,3,4]
        # n = len(A)
        # C = [0] * n
        # mapp = defaultdict(int)
        # for i in range(n):
        #     mapp[A[i]]=max(mapp[A[i]],i)
        #     mapp[B[i]]=max(mapp[B[i]],i)
        # # print(mapp)
        # for i in mapp.values():
        #     C[i] += 1 
        # for i in range(1,n):
        #     C[i]+= C[i-1]
        # return C

        n = len(A)
        mapp = defaultdict(int)
        C = []
        common = 0
        for i in range(n):
            mapp[A[i]]+=1
            if mapp[A[i]] == 2:
                common+=1
            
            mapp[B[i]]+=1
            if mapp[B[i]] == 2:
                common+=1
            
            C.append(common)
        return C
