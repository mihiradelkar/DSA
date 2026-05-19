class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=j=0
        n,m = len(nums1),len(nums2)
        if nums1[0] > nums2[-1] or nums2[0] > nums1[-1]:
            # print("early")
            return -1
        while i<n and j<m:
            # print(i,n,j,m)
            if nums1[i]==nums2[j]:
                return nums1[i]
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
        return -1
