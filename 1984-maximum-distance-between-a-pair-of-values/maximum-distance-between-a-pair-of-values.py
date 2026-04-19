class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1 = [ 55, 30,  5,  4, 2], 
        # nums2 = [100, 20, 10, 10, 5]
        # dist = 0
        # for i in range(len(nums1)):
        #     for j in range(i,len(nums2)):
        #         if nums1[i] <= nums2[j]:
        #             dist = max(dist, j-i)
        # return dist
            
        dist = 0
        m,n = len(nums1),len(nums2)
        i = j = 0
        while i<m and j<n:
            if nums1[i] <= nums2[j]:
                dist = max(dist, j-i)
                j+=1
            else:
                i+=1
                if i > j:
                    j=i
        return dist