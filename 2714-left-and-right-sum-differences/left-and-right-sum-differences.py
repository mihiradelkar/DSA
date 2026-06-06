class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        for i in range(n-1):
            leftSum[i+1] = leftSum[i]+nums[i]
        for i in range(n-1,0,-1):
            rightSum[i-1] = rightSum[i] + nums[i]
        for i in range(n):
            leftSum[i] = abs(leftSum[i]-rightSum[i])
        return leftSum