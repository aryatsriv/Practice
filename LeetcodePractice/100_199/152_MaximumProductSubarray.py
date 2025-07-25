#
# Code
#
#
# Testcase
# Test Result
# Test Result
# 152. Maximum Product Subarray
# Solved
# Medium
# Topics
# conpanies icon
# Companies
# Given an integer array nums, find a subarray that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.
#
#
#
# Example 1:
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd=nums[0]
        minProd=nums[0]
        maxVal=nums[0]

        for num in nums[1:]:
            temp=maxProd
            maxProd=max(maxProd*num,num,minProd*num)
            minProd=min(minProd*num,num,temp*num)
            maxVal=max(minProd,maxProd,maxVal)
        
        return maxVal
