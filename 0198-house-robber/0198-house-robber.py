class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n)
        
        def max_rob(n, nums):
            if n == 0: return 0  # No houses to rob
            if n == 1: return nums[0]  # Only one house

            if dp[n-1]!=-1:
                return dp[n-1]


            dp[n-1] = max(max_rob(n-2,nums)+nums[n-1],max_rob(n-1,nums))

            return dp[n-1]
        


        result = max_rob(n,nums)
        return result

        