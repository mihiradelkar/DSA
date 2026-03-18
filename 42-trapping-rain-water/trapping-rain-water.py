class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1   # two pointers start at ends
        left_max, right_max = 0, 0          # running max from each side
        water = 0

        while left < right:
            if height[left] <= height[right]:
                # left side is the bottleneck — resolve left bar
                if height[left] >= left_max:
                    left_max = height[left]     # update left max, no water here
                else:
                    water += left_max - height[left]  # trapped by left_max ceiling
                left += 1
            else:
                # right side is the bottleneck — resolve right bar
                if height[right] >= right_max:
                    right_max = height[right]   # update right max, no water here
                else:
                    water += right_max - height[right]  # trapped by right_max ceiling
                right -= 1

        return water