class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # question:
        # can nums have negative int/ 0? yes
        # can k = 0 ? yes
        # are te number sorted?
        
        # approach 
        # brute force:try all pairs of values i,j n^2
        # negative number so no two pointers
        # optimal: hash map with prefix 

        # nums    = [ 1, 1, 1] k = 2
        # total   = [ 1, 2, 3]
        # total-k = [-1, 0, 1]
        # prefix_c= {0:1, 1:1, 2:1, 3:1}


        # nums    = [ 1, -1,  1,  1, 1, 1] k = 3
        # total   = [ 1,  0,  1,  2, 3, 4]
        # total-k = [-2, -3, -2, -1, 0, 1]
        # prefix_c= {0:2, 1:2, 2:1, 3:1, 4:1}
        
        prefix_count = {0:1}
        total = 0
        count = 0
        for num in nums:
            total += num
            if (total-k) in prefix_count:
                count += prefix_count[total-k]
            # print(prefix_count)
            prefix_count[total] = prefix_count.get(total,0)+1
        return count


        # old
        # [1,2,1,3,-1]
        prefix_count = {0:1}                        # important to add base case 0:1
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num

            if (prefix_sum-k) in prefix_count:      # sum i - k = sum j : that means the dist is k
                count += prefix_count[prefix_sum-k]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum,0)+1

        return count