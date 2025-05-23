#128. Longest Consecutive Sequence
#Solved
#Medium
#Topics
#Companies
#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
#You must write an algorithm that runs in O(n) time.
#
# 
#
#Example 1:
#
#Input: nums = [100,4,200,1,3,2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#Example 2:
#
#Input: nums = [0,3,7,2,5,8,4,6,0,1]
#Output: 9
#Example 3:
#
#Input: nums = [1,0,1,2]
#Output: 3
# 
#
#Constraints:
#
#0 <= nums.length <= 105
#-109 <= nums[i] <= 109


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        cache = set(nums)
        maxCount=0
        count=0
        for num in cache:
            if num-1 not in cache:
                curr=num
                while curr in cache:
                    count+=1
                    curr+=1
                
            maxCount=max(count,maxCount)
            count=0

        
        return maxCount


